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
    if 'feedback_given' not in st.session_state:
        st.session_state.feedback_given = False

    if prompt := st.chat_input():
        st.session_state.last_prompt = prompt
        process_query(prompt, llm, parser, format_instructions)

    if st.session_state.feedback_given:
        with st.expander("Improve Response"):
            improvement_feedback = st.text_area("How can the response be improved?")
            if st.button("Submit Improvement"):
                new_prompt = f"Improve your previous response.\nOriginal Input : {prompt}\nFeedback: {improvement_feedback}\nPrevious Output: {st.session_state.last_output}\n"
                process_query(new_prompt, llm, parser, format_instructions)
                st.session_state.feedback_given = False

def process_query(prompt, llm, parser, format_instructions):
    st.chat_message("user").write(prompt)
    template = f"Answer the user query.\n{format_instructions}\n{prompt}\n"
    with st.chat_message("assistant"):
        final_model = llm | parser
        response = final_model.invoke(template)
        st.session_state.last_output = response

        user_output = DatabaseOps.save_to_mongodb(response, question=prompt)
        st.write(user_output)

        if st.button("👎 Provide Feedback"):
            st.session_state.feedback_given = True

def handle_feedback(feedback):
    # Implement logic to handle feedback, for now, just a placeholder
    print(feedback)
    return "Feedback recorded."

llm ,parser , format_instructions = setup_once()

create_rule(llm,parser,format_instructions)



    


