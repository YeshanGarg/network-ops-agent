import subprocess

MODEL = "llama3.2"

def chat(history) -> str:
    # Build prompt with system message and conversation history
    prompt = f"{history.system}\n\n"
    
    for msg in history.get():
        role = "User" if msg["role"] == "user" else "Assistant"
        prompt += f"{role}: {msg['content']}\n"
    
    prompt += "Assistant:"
    
    # Call Ollama via subprocess
    result = subprocess.run(
        ["ollama", "run", MODEL, prompt],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    if result.returncode != 0:
        return f"Error calling Ollama: {result.stderr}"
    
    return result.stdout.strip()
