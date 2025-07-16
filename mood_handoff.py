from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

provider = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

mood_helper_agent = Agent(
    name="Mood Helper Agent",
    instructions="""
    You help users feel better when they are sad or stressed.
    Suggest one simple activity like: take a walk, talk to a friend, or listen to music.
    Just give one sentence.
    """,
    model=model
)

mood_analyzer_agent = Agent(
    name="Mood Analyzer Agent",
    instructions="""
    You analyze the user's mood from their message.
    If the mood is 'sad' or 'stressed', you must delegate the task to 'Mood Helper Agent' to support the user.
    Otherwise, respond with: "You're doing well! No help needed."
    """,
    model=model,
    handoffs=[mood_helper_agent]  
)

user_input = input("How are you feeling today?\n")

result = Runner.run_sync(
    mood_analyzer_agent,
    user_input
)


print("\nFinal Response:\n", result.final_output)
