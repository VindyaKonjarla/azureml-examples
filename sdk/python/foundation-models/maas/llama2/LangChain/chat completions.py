from langchain_community.chat_models.azureml_endpoint import AzureMLChatOnlineEndpoint
from langchain.schema import HumanMessage
from langchain.schema import HumanMessage
from dotenv import dotenv_values
from langchain_community.chat_models.azureml_endpoint import (
    AzureMLEndpointApiType,
    LlamaChatContentFormatter,
    AzureMLOnlineEndpoint,
)
config = dotenv_values("key1.env")
config1=dict(config)
chat = AzureMLOnlineEndpoint(
    endpoint_url=config1["API_KEY"],
    endpoint_api_type=AzureMLEndpointApiType.serverless,
    endpoint_api_key=config1["BASE_URL"],
    content_formatter=LlamaChatContentFormatter(),
    model_kwargs={"temperature": 0.8, "max_new_tokens": 400},
)
response = llm.invoke("My name is Julien and I like to")
response
