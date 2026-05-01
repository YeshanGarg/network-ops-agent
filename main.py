from llm import chat
from history import History

SYSTEM = """You are a network operations assistant with deep knowledge
of routing protocols, network configuration, and troubleshooting.
Be concise and technical. When you don't know something, say so."""

def main():
    history = History(system_prompt=SYSTEM)
    print("Network Ops Agent — type 'quit' to exit\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            break

        history.add("user", user_input)
        print("Agent: ", end="", flush=True)

        reply = chat(history)
        print(reply)
        print()

        history.add("assistant", reply)

if __name__ == "__main__":
    main()
