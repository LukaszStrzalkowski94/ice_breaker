from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import os

if __name__ == '__main__':
    print("hello Lang chain")
    print(os.environ['OPENAI_API_KEY'])
