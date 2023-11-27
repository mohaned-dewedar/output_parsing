import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from database import DatabaseOps
from pydantic_inputs import Rules
from dotenv import load_dotenv  
import logging



@st.cache_resource()
def setup_once():
    load_dotenv()
    model_name = 'gpt-4-1106-preview'
    # model_name = 'gpt-3.5-turbo'

    DatabaseOps.connect()
    llm = ChatOpenAI(temperature=0,model=model_name)
    parser = PydanticOutputParser(pydantic_object=Rules)
    format_instructions = parser.get_format_instructions()

    return llm, parser, format_instructions , model_name


def process_and_save_rule(question,prompt, final_model,model_name):
    try:
        response = final_model.invoke(prompt)
        user_output, message_id = DatabaseOps.save_to_mongodb(response, question=question,model_name=model_name)
        st.json(user_output)  # Display the JSON in a formatted way
        st.success(f"Rule saved with associated message ID: {message_id}")
        return user_output, message_id
    except Exception as e:
        logging.exception("An error occurred: {str(e)}")
        st.error(f"An error occurred: {str(e)}")
        return None, None

def create_rule(llm, parser, format_instructions,model_name):
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        template = f"Answer the user query.\n{format_instructions}\n{prompt}\n"
        with st.chat_message("assistant"):
            final_model = llm | parser
            process_and_save_rule(prompt,template, final_model,model_name)

llm ,parser , format_instructions, model_name = setup_once()

create_rule(llm,parser,format_instructions,model_name)



    


