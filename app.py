from flask import Flask, request, jsonify

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

from chatbot import myself, bot

@app.route("/response.json")
def response():
	return jsonify({'result': "I don't know"})

@app.route("/")
def home():
    return chatbot_html + "<script>let getResp = webGetResp;</script>"

app.run()