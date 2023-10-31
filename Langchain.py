from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import os

information = """Jerzy VI (ang. George VI, ur. 14 grudnia 1895 w Sandringham House, zm. 6 lutego 1952 tamże) – król Zjednoczonego Królestwa Wielkiej Brytanii i Irlandii Północnej i dominiów (1936–1952), cesarz Indii (1936–1947), król Indii (1947–1949), król Irlandii (1936–1949). Brat Edwarda VIII i jego następca (po abdykacji Edwarda) oraz ojciec Elżbiety II.
 """

if __name__ == '__main__':
    print("hello Lang chain")
    
    summary_template = """given the Linkedin information {information} about a person from I want you to create:
                        1. a short summary 
                        2. two interesting facts about them 
                        """

summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

chain = LLMChain(llm=llm, prompt = summary_prompt_template)

print(chain.run(information=information))