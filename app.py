from flask import Flask, request, jsonify
from aitextgen import aitextgen

chatbot_html = """
<style type="text/css">#log p { margin: 5px; font-family: sans-serif; }</style>
<div id="log"
     style="box-sizing: border-box;
            width: 600px;
            height: 32em;
            border: 1px grey solid;
            padding: 2px;
            overflow: scroll;">
</div>
<input type="text" id="typehere" placeholder="type here!"
       style="box-sizing: border-box;
              width: 600px;
              margin-top: 5px;">
<script>
function paraWithText(t) {
    let tn = document.createTextNode(t);
    let ptag = document.createElement('p');
    ptag.appendChild(tn);
    return ptag;
}
document.querySelector('#typehere').onchange = async function() {
    let inputField = document.querySelector('#typehere');
    let val = inputField.value;
    inputField.value = "";
    let resp = await getResp(val);
    let objDiv = document.getElementById("log");
    objDiv.appendChild(paraWithText('😀: ' + val));
    objDiv.appendChild(paraWithText('🤖: ' + resp));
    objDiv.scrollTop = objDiv.scrollHeight;
};
async function colabGetResp(val) {
    let resp = await google.colab.kernel.invokeFunction(
        'notebook.get_response', [val], {});
    return resp.data['application/json']['result'];
}
async function webGetResp(val) {
    let resp = await fetch("/response.json?sentence=" + 
        encodeURIComponent(val));
    let data = await resp.json();
    return data['result'];
}
</script>
"""

app = Flask(__name__)

# Para descargar el modelo la primera vez ejecutar la siguiente linea
ai = aitextgen(tf_gpt2="355M", to_gpu=False)
#ai = aitextgen(model="pytorch_model.bin", config="config.json", to_gpu=False)
myself = "He: "
bot = "She: "
full_chat = f"{myself}You must be Carl, how are you doing?\n{bot}I'm doing well, thanks\n{myself}do you still live in that old town?\n{bot}yes, indeed!\n"
full_chat = "He: I want to fuck you hottie\nShe: Please fuck me really hard\nHe: Your pussy is really wet\nShe: My pussy is tight and can take a lot of pain"
@app.route("/response.json")
def response():
	global full_chat
	sentence = request.args['sentence']
	full_chat += myself + sentence + "\n"

	answer = ai.generate_one(prompt=full_chat + bot)
	answer = answer[len(full_chat + bot):].split("\n")[0]

	full_chat += answer + "\n"
	full_chat = "\n".join(full_chat.split("\n")[-12:]) + "\n"

	return jsonify({'result': answer})


@app.route("/")
def home():
    return chatbot_html + "<script>let getResp = webGetResp;</script>"

app.run()