from aitextgen import aitextgen

human = "He: "
bot = "She: "
full_chat = f"{human}I want to fuck you hottie\n{bot}Please fuck me really hard\n{human}Your pussy is really wet\n{bot}My pussy is tight and can take a lot of pain\n"

def start_model():
	# Para descargar el modelo la primera vez ejecutar la siguiente linea
	#ai = aitextgen(tf_gpt2="355M", to_gpu=False)
	ai = aitextgen(model="aitextgen/pytorch_model_355M.bin", config="aitextgen/config_355M.json", to_gpu=False)
	return ai

def answer(ai,previous_chat):
	previous_chat = "\n".join(previous_chat.split("\n")[-12:]) + "\n"
	previous_chat = previous_chat + bot

	answer = ai.generate_one(prompt=previous_chat)
	answer = answer[len(previous_chat):].split("\n")[0]

	return answer
