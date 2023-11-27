from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from database import DatabaseOps
from pydantic_inputs import Rules
from dotenv import load_dotenv  
load_dotenv()
DatabaseOps.connect()
llm = ChatOpenAI(temperature=0,model='gpt-4-1106-preview')
parser = PydanticOutputParser(pydantic_object=Rules)
format_instructions = parser.get_format_instructions()
final_model = llm | parser
app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    global format_instructions , final_model
    user_message = request.json.get('message')
    # Process the message with your AI model
    template = f"Answer the user query.\n{format_instructions}\n{user_message}\n"
    response = final_model.invoke(template)
    user_output = DatabaseOps.save_to_mongodb(response, question=user_message)
    return jsonify(response.model_dump_json())

def process_message(message):
    # Placeholder for your AI logic
    return "This is a response from the AI."

if __name__ == '__main__':
    app.run(debug=True)
