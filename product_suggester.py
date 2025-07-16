from agents import Agent , AsyncOpenAI , OpenAIChatCompletionsModel , Runner , RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=provider
)

config = RunConfig(
    model = model,
    model_provider=provider,
    tracing_disabled=True
)

agent = Agent(
    name="Smart Store Agent",
    instructions="""
    You are a helpful store agent.
    When a user tells you their symptoms or needs (like headache, cold, fever, body pain), 
    suggest a suitable product or medicine and explain why it helps.
    Be clear, friendly, and helpful.
    """,
    model=model
)

user_input = input("🧑 What do you need help with today? (e.g., I have a headache): ")

result = Runner.run_sync(
    agent,
    user_input,
    run_config=config
)

print(result.final_output)