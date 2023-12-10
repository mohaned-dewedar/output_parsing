# Streamlit App - Rule Generator with GPT-4 and MongoDB

## Overview
This Streamlit application leverages OpenAI's GPT-4 model to generate and save rules based on user inputs. It includes a setup for initializing the language model and connecting to a MongoDB database for persistent storage. The application also utilizes a Pydantic output parser to define and format the expected output.

## Features
- **Model Initialization**: Sets up the GPT-4 model and database connection, cached for the app's lifetime.
- **Rule Generation**: Takes user input to generate rules using GPT-4.
- **Database Integration**: Processes and saves generated rules to MongoDB.
- **Output Formatting**: Uses a Pydantic output parser for structured output.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/mohaned-dewedar/output_parsing.git]

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. Set Environment Variables with OpenAI api key and Mongodb connection string in your .env file


## Usage
1. **Run the app**

```bash
  streamlit run streamlit_app.py
```    

2. **Interact with the Chatbot**  
    A- Input a Rule description
    B-The app processes the input, generates a rule using GPT-4, and saves it to MongoDB.
    C-View the generated rule and its details in the app interface.

## Tech Stack
1. **Streamlit** For creating the web app interface.
2. **OpenAI's GPT Models**: For generating responses based on user inputs.
3. **MongoDB**: For storing and retrieving generated rules.
4. **Python**: Core programming language.
5. **Pydantic**: For output parsing and formatting.





   
