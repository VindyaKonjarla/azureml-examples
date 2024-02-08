from langchain_community.chat_models.azureml_endpoint import AzureMLChatOnlineEndpoint
from langchain.schema import HumanMessage
from langchain.schema import HumanMessage
from dotenv import dotenv_values
from langchain_community.chat_models.azureml_endpoint import (
    AzureMLEndpointApiType,
    LlamaChatContentFormatter,
)
config = dotenv_values("key1.env")#Load the environmet variable from the .env file
config1=dict(config)   # converting into key and values from the list
chat = AzureMLChatOnlineEndpoint(
    endpoint_url=config1["BASE_URL"], # Load the URL from the .env file
    endpoint_api_type=AzureMLEndpointApiType.serverless,#It determines the communication protocol and format used to send and receive data between clients and the deployed model
    endpoint_api_key=config1["API_KEY"],# Load the primary/secondary key or AMLToken for the endpoint from the .env file
    content_formatter=LlamaChatContentFormatter(),#The content_formatter parameter is a handler class for transforming the request and response of an AzureML endpoint to match with required schema
    model_kwargs={"temperature": 0.8}, #temperature value defines the accuracy of the output
)
response = chat.invoke(
    [HumanMessage(content="Will the Collatz conjecture ever be solved?")],# fetching the output from endpoint
    max_tokens=512,
)
response
