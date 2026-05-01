class History:
    def __init__(self, system_prompt: str):
        self.system = system_prompt
        self.messages = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def get(self):
        return self.messages
