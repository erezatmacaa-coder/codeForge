TOOL = {
    "type": "function",
    "function": {
        "name": "think",
        "description": "Use this to reason about the task and plan your approach before taking actions.",
        "parameters": {
            "type": "object",
            "properties": {
                "thought": {
                    "type": "string",
                    "description": "Your internal reasoning and plan."
                }
            },
            "required": ["thought"],
        },
    },
}


def execute(thought):
    return f"[Plan]: {thought}"
