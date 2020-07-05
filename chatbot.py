#from aitextgen import aitextgen
import time

human = "He: "
bot = "She: "
full_chat = f"{human}I want to fuck you hottie\n{bot}Please fuck me really hard\n{human}Your pussy is really wet\n{bot}My pussy is tight and can take a lot of pain\n"

def start_model():
	# Para descargar el modelo la primera vez ejecutar la siguiente linea
	#ai = aitextgen(tf_gpt2="355M", to_gpu=False)
	ai = aitextgen(model="pytorch_model.bin", config="config.json", to_gpu=False)

def answer(previous_chat):
	previous_chat = "\n".join(previous_chat.split("\n")[-12:]) + "\n"
	previous_chat = previous_chat + bot

	answer = ai.generate_one(prompt=previous_chat)
	answer = answer[len(full_chat + bot):].split("\n")[0]

	return answer