import os

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a file at the given path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file"
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file. Creates the file and parent directories if needed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file"
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write"
                    }
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": "Edit a file by replacing the first occurrence of old_string with new_string.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file"
                    },
                    "old_string": {
                        "type": "string",
                        "description": "Text to find"
                    },
                    "new_string": {
                        "type": "string",
                        "description": "Text to replace it with"
                    }
                },
                "required": ["path", "old_string", "new_string"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files and directories at a given path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to list"
                    }
                },
                "required": ["path"],
            },
        },
    },
]


def execute(name, args):
    if name == "read_file":
        path = args["path"]
        if not os.path.exists(path):
            return f"Error: File not found: {path}"
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    elif name == "write_file":
        path = args["path"]
        content = args["content"]
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Successfully wrote {len(content)} characters to {path}"
        except Exception as e:
            return f"Error writing file: {e}"

    elif name == "edit_file":
        path = args["path"]
        old = args["old_string"]
        new = args["new_string"]
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            if old not in content:
                return f"Error: Could not find specified text in {path}"
            content = content.replace(old, new, 1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Successfully edited {path}"
        except Exception as e:
            return f"Error editing file: {e}"

    elif name == "list_files":
        path = args["path"]
        if not os.path.exists(path):
            return f"Error: Path not found: {path}"
        try:
            items = os.listdir(path)
            result = []
            for item in sorted(items):
                full = os.path.join(path, item)
                if os.path.isdir(full):
                    result.append(f"{item}/")
                else:
                    result.append(item)
            return "\n".join(result)
        except Exception as e:
            return f"Error listing files: {e}"

    return f"Error: Unknown file operation: {name}"
