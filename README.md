# LangChain-Assistant
# Gemini-1.5-Pro Chatbot with LangChain 

This project is a simple chatbot built using **Google's Gemini-1.5-Pro** model via **LangChain**, deployed with **Streamlit**. The chatbot takes user input and generates AI-powered responses.

## Features
- Uses **Google Gemini-1.5-Pro** for generating responses.
- Built with **LangChain** for easy AI model integration.
- **Streamlit** for a simple and interactive web interface.
- Supports environment variable management with **dotenv**.
- Easily configurable via `requirements.txt`.

## Installation  

###
1. Clone the Repository

2. Create a Virtual Environment
  python -m venv venv

3. Activate the Virtual Environment

Windows:    venv\Scripts\activate

Mac/Linux:   source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Set Up Environment Variables
Create a .env file in the root directory and add your Google API key:
GOOGLE_API_KEY="your-api-key-here"
Or, rename the provided .env.txt file to .env.

6 Run the Application
streamlit run prompts.py
 
Dependencies:
The required libraries are listed in requirements.txt.

### Key dependencies include:

LangChain (langchain, langchain-google-genai)
Streamlit (streamlit)
Dotenv (python-dotenv)

Contributing
Feel free to contribute by submitting issues or pull requests.

License
This project is licensed under MIT License.
