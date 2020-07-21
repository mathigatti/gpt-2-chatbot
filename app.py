from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask import render_template
import time
from googletrans import Translator


app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run

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

def translate(text,target_lang="es"):
    translator = Translator()
    return translator.translate(text, dest=target_lang).text


@app.route("/response.json")
def response():
    human_answer = translate(request.args['sentence'],"en")
    chat = request.args['chat']

    update_chat(chat,human + human_answer + "\n")
    bot_answer = answer(read_chat(chat))
    update_chat(chat,bot + bot_answer + "\n")

    return jsonify({'result': translate(bot_answer,"es")})

@app.route("/")
def home():
    chat = generate_chat()
    return render_template('index.html',chat=chat)

app.run()
