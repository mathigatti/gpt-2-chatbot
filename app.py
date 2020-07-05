from flask import Flask, request, jsonify
from flask import render_template
import time

app = Flask(__name__)

from chatbot import human, bot, full_chat, answer

def generate_chat():
    chat_path = "chats/" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    with open(chat_path,'w') as f:
        f.write(full_chat)
    return chat_path

def update_chat(chat_path,answer):
    with open(chat_path,'a') as f:
        f.write(answer)

def read_chat(chat_path):
    with open(chat_path,'r') as f:
        chat_text = f.read()
    return chat_text

@app.route("/response.json")
def response():
    human_answer = request.args['sentence']
    chat = request.args['chat']

    update_chat(chat,human + human_answer + "\n")    
    bot_answer = answer(read_chat(chat))
    update_chat(chat,bot + bot_answer + "\n")

    return jsonify({'result': bot_answer})

@app.route("/")
def home():
    chat = generate_chat()
    return render_template('index.html',chat=chat)

app.run()