import asyncio
from agent_framework import ChatAgent, AgentThread
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI

async def test_memory_with_threads():
    local_client = AsyncOpenAI(
        api_key="dummy_key",
        base_url="http://localhost:11434/v1"
    )
    
    client = OpenAIChatClient(
        async_client=local_client,
        model_id="llama3.2"
    )
    
    print("Testing Multi-turn Memory with Explicit Thread\n")
    
    agent = ChatAgent(
        chat_client=client,
        instructions="You are a helpful assistant. Remember what users tell you.",
        name="MemoryBot"
    )
    
    # Create a thread to maintain conversation state
    thread = AgentThread()
    
    # Turn 1
    result1 = await agent.run("My name is Alex and I live in Tokyo.", thread=thread)
    print(f"User: My name is Alex and I live in Tokyo.")
    print(f"Bot: {result1.text}\n")
    
    # Turn 2
    result2 = await agent.run("What's my name?", thread=thread)
    print(f"User: What's my name?")
    print(f"Bot: {result2.text}\n")
    
    # Turn 3
    result3 = await agent.run("Where do I live?", thread=thread)
    print(f"User: Where do I live?")
    print(f"Bot: {result3.text}\n")

asyncio.run(test_memory_with_threads())