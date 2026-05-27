import argparse
import sys
from agent.core import Agent


def print_banner():
    print("╔══════════════════════════════════════════╗")
    print("║        CodeForge v1.0                     ║")
    print("║     AI-powered coding assistant           ║")
    print("╚══════════════════════════════════════════╝")


def interactive_mode(agent):
    print_banner()
    print("Interactive mode. Type 'exit' to quit, 'reset' to start over.\n")

    while True:
        try:
            user_input = input(">>> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            break
        if user_input.lower() == "reset":
            agent.reset()
            print("Conversation reset.\n")
            continue

        try:
            response = agent.run(user_input)
            print(response)
        except Exception as e:
            print(f"Error: {e}")


def single_mode(agent, prompt):
    try:
        response = agent.run(prompt)
        print(response)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CodeForge - AI-powered coding assistant"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Direct prompt (omit for interactive mode)",
    )
    args = parser.parse_args()

    agent = Agent()

    if args.prompt:
        single_mode(agent, args.prompt)
    else:
        interactive_mode(agent)


if __name__ == "__main__":
    main()
