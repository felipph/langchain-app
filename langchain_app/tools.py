from dotenv import load_dotenv
from langchain.chat_models.azure_openai import AzureChatOpenAI
import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate


load_dotenv()

chat_llm = AzureChatOpenAI(
    openai_api_type=os.getenv('AZOPENAI_API_TYPE'),
    openai_api_key=os.getenv('AZOPENAI_API_KEY'),
    openai_api_base=os.getenv('AZOPENAI_API_BASE'),
    openai_api_version=os.getenv('AZOPENAI_DEPLOYMENT_VERSION'),
    deployment_name=os.getenv('AZOPENAI_DEPLOYMENT_NAME'),
    model=os.getenv('AZOPENAI_MODEL_NAME'),
)

def ideia_viagem(interesse, custo):
    template_user = """Por favor faça uma sugestão detalhada de viagem que tenha como orçamento máximo de R$ {orcamento} """
    template_machine = """Você é um especialista em viagens no Brasil com o foco em {interesse} e deve dar informações de roteiros de forma detalhada,
    onde deve ser apresentados os custos de cada atividade. """
    
    ctpl_user = ChatPromptTemplate.from_template(template_user)
    ctpl_ai   = ChatPromptTemplate.from_template(template_machine)
    
    chat_prompt = ChatPromptTemplate.from_messages([ctpl_ai, ctpl_user])
    interaction_messages = chat_prompt.format_messages(
                    interesse=interesse,
                    orcamento=custo)
    
    return chat_llm(interaction_messages).content

print(ideia_viagem("praia e compras", "5000"))
    
