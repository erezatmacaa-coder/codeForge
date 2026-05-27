from . import llm, config
from .prompts import SYSTEM_PROMPT
from .tools import get_all_tools, execute_tool


class Agent:
    def __init__(self, system_prompt=None):
        self.messages = [
            {"role": "system", "content": system_prompt or SYSTEM_PROMPT}
        ]

    def _trim_history(self):
        if len(self.messages) > config.MAX_HISTORY_MESSAGES:
            keep = self.messages[:1]
            keep.extend(self.messages[-(config.MAX_HISTORY_MESSAGES - 1):])
            self.messages = keep

    def run(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

        for iteration in range(config.MAX_TOOL_ITERATIONS):
            response = llm.chat(self.messages, tools=get_all_tools())

            if response.tool_calls:
                assistant_msg = {
                    "role": "assistant",
                    "content": response.content or "",
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": "function",
                            "function": {
                                "name": tc.function.name,
                                "arguments": tc.function.arguments,
                            },
                        }
                        for tc in response.tool_calls
                    ],
                }
                self.messages.append(assistant_msg)

                for tool_call in response.tool_calls:
                    result = execute_tool(tool_call)
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result),
                    })
            else:
                self.messages.append({
                    "role": "assistant",
                    "content": response.content or "",
                })
                self._trim_history()
                return response.content or ""

        self._trim_history()
        return "Maximum iterations reached. Please refine your request."

    def reset(self):
        self.messages = [self.messages[0]]
