from aitextgen import aitextgen

myself = "He: "
bot = "She: "
full_chat = f"{myself}: I want to fuck you hottie\n{bot}: Please fuck me really hard\n{myself}: Your pussy is really wet\n{bot}: My pussy is tight and can take a lot of pain"


def start_model():
	# Para descargar el modelo la primera vez ejecutar la siguiente linea
	ai = aitextgen(tf_gpt2="355M", to_gpu=False)
	#ai = aitextgen(model="pytorch_model.bin", config="config.json", to_gpu=False)


def answer():
	global full_chat
	sentence = request.args['sentence']
	full_chat += myself + sentence + "\n"

	answer = ai.generate_one(prompt=full_chat + bot)
	answer = answer[len(full_chat + bot):].split("\n")[0]

	full_chat += answer + "\n"
	full_chat = "\n".join(full_chat.split("\n")[-12:]) + "\n"
