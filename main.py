from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
load_dotenv()

def main():
    print("Hello from langchain-course!")

    information = """
    Elon Reeve Musk (wym. /ˈi:lɒn ˈmʌsk/; ur. 28 czerwca 1971 w Pretorii[4]) – południowoafrykański przedsiębiorca, założyciel, 
    współzałożyciel lub finansista przedsiębiorstw SpaceX, Tesla, Neuralink, X.com (część firmy PayPal), 
    The Boring Company[5] oraz xAI. Pochodzi z Republiki Południowej Afryki, mieszka i pracuje w Stanach Zjednoczonych (posiada obywatelstwo południowoafrykańskie, kanadyjskie i amerykańskie). 
    Dyrektor generalny i techniczny w SpaceX, dyrektor generalny i główny architekt w Tesla Inc.
    W styczniu 2021 został uznany najbogatszym człowiekiem świata przez magazyn „Forbes” i agencję Bloomberg﻿[w innych językach][6][7][8]. 
    Od 28 października 2022 właściciel serwisu X (kiedyś „Twitter”). W okresie od 20 stycznia do 28 maja 2025 szef Departamentu Wydajności Rządu﻿[w innych językach] 
    (ang. Department of Government Efficiency, DOGE) w drugim gabinecie Donalda Trumpa. Na dzień 16 czerwca 2026 roku, według magazynu „Forbes”, 
    jego majątek szacowany jest na 1,3 biliona dolarów amerykańskich (USD)[1].
"""

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
        )


    llm = ChatOllama(temperature=0, model="gemma3:4b")
    chain = summary_prompt_template | llm

    response = chain.invoke({"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
