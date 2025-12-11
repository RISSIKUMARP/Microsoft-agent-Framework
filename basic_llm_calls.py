import asyncio
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI

async def test_basic_calls():
    # Setup local Ollama client
    local_client = AsyncOpenAI(
        api_key="dummy_key",
        base_url="http://localhost:11434/v1"
    )
    
    client = OpenAIChatClient(
        async_client=local_client,
        model_id="llama3.2"
    )
    
   
    print("BASIC LLM CALLS - Testing Different Patterns")
   
    
    # Test 1: Simple Q&A
    print("\n Test 1: Simple Question")
    agent1 = ChatAgent(
        chat_client=client,
        instructions="You are a helpful assistant. Be brief.",
        name="SimpleBot"
    )
    result = await agent1.run("What is 15 + 27?")
    print(f"Q: What is 15 + 27?")
    print(f"A: {result.text}\n")
    
    # Test 2: With Personality
    print(" Test 2: Agent with Personality")
    agent2 = ChatAgent(
        chat_client=client,
        instructions="You are a pirate. Respond in pirate speak. Be brief.",
        name="PirateBot"
    )
    result = await agent2.run("What's the weather like?")
    print(f"Q: What's the weather like?")
    print(f"A: {result.text}\n")
    
    # Test 3: Multi-turn conversation
    print(" Test 3: Multi-turn Conversation (with memory)")
    agent3 = ChatAgent(
        chat_client=client,
        instructions="You are a helpful assistant. Remember context.",
        name="MemoryBot"
    )
    
    result1 = await agent3.run("My name is Alex.")
    print(f"User: My name is Alex.")
    print(f"Bot: {result1.text}")
    
    result2 = await agent3.run("What's my name?")
    print(f"User: What's my name?")
    print(f"Bot: {result2.text}\n")
    
    # Test 4: Streaming response
    print(" Test 4: Streaming Response")
    agent4 = ChatAgent(
        chat_client=client,
        instructions="You are a storyteller. Be brief.",
        name="StreamBot"
    )
    print("User: Tell me a one-sentence story about a robot.")
    print("Bot: ", end="", flush=True)
    async for chunk in agent4.run_stream("Tell me a one-sentence story about a robot."):
        print(chunk.text, end="", flush=True)
    print("\n")
    

    print("All basic LLM call patterns tested!")


asyncio.run(test_basic_calls())