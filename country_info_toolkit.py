from agents import Agent , AsyncOpenAI , OpenAIChatCompletionsModel , Runner , RunConfig , function_tool
from dotenv import load_dotenv
import os

import requests



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

@function_tool
def get_capital(country:str) -> str:
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()[0]
        capital = data.get("capital",["Unknown"][0])
        return capital 
    except Exception as e:
        return f" Couldn't fetch capital: {str(e)}"
    
@function_tool
def get_language(country:str) -> str:
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()[0]
        langs = list(data.get("languages", {}).values())
        return ", ".join(langs) if langs else "Unknown"
    except Exception as e:
        return f"Couldn't fetch language: {str(e)}"
    
@function_tool
def get_population(country:str) -> str:
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()[0]
        pop = data.get("population","Unknown")
        return f"{pop:,}"
    except Exception as e:
        return f"Couldn't fetch population: {str(e)}"
    




orchestrator_agent = Agent(
    name = "Country Info Bot",
    instructions='''
    You are a smart country information agent
    the user will give you the name of country and use the
    available tools to get the capital , language and population of country and then respond in this format:
    Country: <country>
    Capital: <capital>
    Language(s): <language>
    Population: <population>
    
    ''',
    model=model,
    tools=[get_capital,get_language,get_population]
)

user_input = input("Please Enter The Country Name : ")
result = Runner.run_sync(
    orchestrator_agent,
    user_input,
    run_config=config
)

print(result.final_output)
    

