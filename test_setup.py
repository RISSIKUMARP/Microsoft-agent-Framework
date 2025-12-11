import asyncio
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI

async def test():
    # Use local Ollama instead of OpenAI
    local_client = AsyncOpenAI(
        api_key="dummy_key",  # Ollama doesn't need real key
        base_url="http://localhost:11434/v1"
    )
    
    client = OpenAIChatClient(
        async_client=local_client,
        model_id="llama3.2"
    )
    
    agent = ChatAgent(
        chat_client=client,
        instructions="You are a helpful assistant.",
        name="TestBot"
    )
    
    result = await agent.run("Say 'Setup successful!' if you can read this.")
    print(result.text)

asyncio.run(test())