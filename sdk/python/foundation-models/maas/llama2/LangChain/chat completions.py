#AzureMLEndpointApiType:It determines the communication protocol and format used to send and receive data between clients and the deployed model

#AzureMLOnlineEndpoint:It provides functionalities to send text prompts to the model and receive its responses.

#endpoint_url: This specifies the base URL of the deployed endpoint where the LLM is running. You likely obtained this from config1["BASE_URL"]

#endpoint_api_type: This sets the type of API used by the endpoint.

#endpoint_api_key: This provides the necessary authorization key to access the endpoint. You probably got this from config1["API_KEY"].

#content_formatter: This defines how input and output data are formatted for the LLM.

#model_kwargs: This is a dictionary of additional arguments passed to the model. Here, you're setting the "temperature" to 0.8, which controls the randomness of the generated text (higher values lead to more creativity but potentially less coherence).

#chat.invoke(): This method sends the provided message(s) to the LLM and retrieves its response.

#HumanMessage:is used to represent messages originating from a human user in the context of the langchain library.

#dotenv_values():It allows you to read key-value pairs from a .env file and return them as a dictionary 

#.env: It is an environment file where the API key and model URL are stored.

#The environment file should be in the same root directory.

from langchain_community.chat_models.azureml_endpoint import AzureMLChatOnlineEndpoint
from langchain.schema import HumanMessage
from langchain.schema import HumanMessage
from dotenv import dotenv_values
from langchain_community.llms.azureml_endpoint import (
    AzureMLEndpointApiType,
    LlamaContentFormatter,
    AzureMLOnlineEndpoint,
)
config = dotenv_values(".env") 
config1=dict(config)   
llm = AzureMLOnlineEndpoint(
    endpoint_url=config1["BASE_URL"], 
    endpoint_api_type=AzureMLEndpointApiType.serverless,
    endpoint_api_key=config1["API_KEY"], 
    content_formatter=LlamaContentFormatter(),
    model_kwargs={"temperature": 0.8, "max_new_tokens": 400},
)
response = llm.invoke("My name is Julien and I like to")
response
