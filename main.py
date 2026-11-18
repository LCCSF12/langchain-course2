from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    
    Alberto Santos Dumont (Palmira, 20 de julho de 1873 – Guarujá, 23 de julho de 1932) foi um aeronauta, esportista, autodidata e inventor brasileiro.[1][2][3][4] Santos Dumont projetou, construiu e voou os primeiros balões dirigíveis com motor a gasolina. Esse mérito lhe é garantido internacionalmente pela conquista do Prêmio Deutsch em 1901, quando em um voo contornou a Torre Eiffel com o seu dirigível Nº 6, transformando-se em uma das pessoas mais famosas do mundo durante o século XX.[5]

Santos Dumont também foi o primeiro a decolar a bordo de um avião impulsionado por um motor a gasolina. Em 23 de outubro de 1906, voou cerca de sessenta metros a uma altura de dois a três metros com o Oiseau de Proie (francês para "ave de rapina"), no Campo de Bagatelle, em Paris. Menos de um mês depois, em 12 de novembro, diante de uma multidão de testemunhas, percorreu 220 metros a uma altura de seis metros com o Oiseau de Proie III. Esses voos foram os primeiros homologados pelo Aeroclube da França de um aparelho mais pesado que o ar,[6] e possivelmente a primeira demonstração pública de um veículo levantando voo por seus próprios meios, sem a necessidade de uma rampa para lançamento.[7]

O título de responsável pelo primeiro voo num avião, atribuído por brasileiros a Santos Dumont, é disputado com outros pioneiros, nomeadamente os irmãos Wright. Na França, costuma-se atribuir o feito a Clément Ader, que teria efetuado o primeiro voo de um equipamento mais pesado que o ar, a aeronave a vapor Ader Éole,[8] propulsionado por um motor a vapor de 20 CV[9] e levantando voo pelos seus próprios meios em 9 de outubro de 1890,[10][11][12] mas teve suas alegações refutadas pelo Ministério da Guerra do Exército Francês.[13][14] Ao redor do mundo, pelo menos catorze nomes são citados como inventores do avião.[13]

    """
    summary_template = """
    give the information  {information} about a person i want to create:
    1. A short summary 
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="gemma3:270m")
    chain = summary_prompt_template | llm
    
    response = chain.invoke({"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
