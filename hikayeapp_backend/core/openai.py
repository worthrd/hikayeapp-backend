from langchain_openai import AzureChatOpenAI
from hikayeapp_backend.config import settings
from dotenv import load_dotenv

load_dotenv()

class StoryOpenAI:
    @staticmethod
    def create_story(prompt_from_human:str) -> str:
        llm = AzureChatOpenAI(azure_deployment=settings.AZURE_DEPLOYMENT,
                              api_version=settings.AZURE_API_VERSION)

        messages = [("system", 
                     "You are helpful AI assistan that you create child stories based user input there will be no violance"),
                    ("human", prompt_from_human)]

        ai_msg = llm.invoke(messages)
        return ai_msg.content
