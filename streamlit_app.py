import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from database import DatabaseOps
from pydantic_inputs import Rules
from dotenv import load_dotenv  




@st.cache_resource()
def setup_once():
    load_dotenv()
    DatabaseOps.connect()
    llm = ChatOpenAI(temperature=0,model='gpt-4-1106-preview')
    parser = PydanticOutputParser(pydantic_object=Rules)
    format_instructions = parser.get_format_instructions()

    return llm, parser, format_instructions


def create_rule(llm, parser, format_instructions):
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        template = f"Answer the user query.\n{format_instructions}\n{prompt}\n"
        with st.chat_message("assistant"):
            try:
                final_model = llm | parser
                response = final_model.invoke(template)
                user_output = DatabaseOps.save_to_mongodb(response,question=prompt)
                st.write(user_output)
            except Exception as e:
                error = str(e)
                new_prompt = f"The following error occurred: {error}\nSee if you can correct the json output and try again\n {format_instructions}\n The user's request was {prompt}" 
                response = final_model.invoke(template)
                user_output = DatabaseOps.save_to_mongodb(response,question=prompt)
                st.write(user_output)


llm ,parser , format_instructions = setup_once()

create_rule(llm,parser,format_instructions)



    


