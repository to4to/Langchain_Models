from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a prompt template
prompt_template = ChatPromptTemplate.from_template(
    "You are a helpful assistant. {question}"
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Generate a response
response = chain.run(question="What is Python?")
print(response)