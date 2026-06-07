import os
import ollama

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "amazon.nova-lite-v1:0")


def chat(messages: list[dict]) -> str:
    """
    Central LLM provider router.

    Local/dev:
      LLM_PROVIDER=ollama

    AWS/prod:
      LLM_PROVIDER=bedrock
    """

    if LLM_PROVIDER == "ollama":
        client = ollama.Client(host=OLLAMA_HOST)
        response = client.chat(
            model=OLLAMA_MODEL,
            messages=messages,
        )
        return response["message"]["content"]

    if LLM_PROVIDER == "bedrock":
        raise NotImplementedError(
            "Bedrock provider is not implemented yet. Next step: add boto3 Bedrock Runtime client."
        )

    raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
