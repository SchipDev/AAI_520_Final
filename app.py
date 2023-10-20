from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from model import ChatBot

app = Flask(__name__)
bot = ChatBot()

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
    return bot.generate_response(user_message)

if __name__ == '__main__':
    print("running")
    app.run()
