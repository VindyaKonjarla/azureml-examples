from langchain_community.chat_models.azureml_endpoint import AzureMLChatOnlineEndpoint
from langchain.schema import HumanMessage
from langchain.schema import HumanMessage
from dotenv import dotenv_values
from langchain_community.chat_models.azureml_endpoint import (
    AzureMLEndpointApiType,
    LlamaChatContentFormatter,
)
config = dotenv_values("key1.env")
config1=dict(config)
chat = AzureMLChatOnlineEndpoint(
    endpoint_url=config1["KEY"],
    endpoint_api_type=AzureMLEndpointApiType.serverless,
    endpoint_api_key=config1["BASE_URL"],
    content_formatter=LlamaChatContentFormatter(),
    model_kwargs={"temperature": 0.8},
)
response = chat.invoke(
    [HumanMessage(content="Will the Collatz conjecture ever be solved?")],
    max_tokens=512,
)
response
