from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
#from werkzeug import url_quote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_message = request.form['user_message']
    # Replace this with your chatbot logic
    bot_response = get_bot_response(user_message)
    return jsonify({'bot_response': bot_response})

def get_bot_response(user_message):
    # Replace this function with your chatbot's response logic
    # Simple example: Echo the user's message
    return "Hello, I am still being set up!"

if __name__ == '__main__':
    print("running")
    app.run()
