from aitextgen import aitextgen

human = "He: "
bot = "She: "
full_chat = f"{human}I want to fuck you hottie\n{bot}Please fuck me really hard\n{human}Your pussy is really wet\n{bot}My pussy is tight and can take a lot of pain\n"
#full_chat = f"{human}My lord, how can I stop this pain?.\n{bot}This will stop the day the truthful will benefit from their truthfulness.\n{human} Thanks my lord, for them are gardens in Paradise to live forever.\n{bot}Those who follower me will be rewarded, my son.\n"

def start_model():
	# Para descargar el modelo la primera vez ejecutar la siguiente linea
	#ai = aitextgen(tf_gpt2="355M", to_gpu=True)
	ai = aitextgen(model="aitextgen/pytorch_model_355M.bin", config="aitextgen/config_355M.json", to_gpu=True)
	return ai

ai = start_model()

def answer(previous_chat):
	previous_chat = "\n".join(previous_chat.split("\n")[-12:]) + "\n"
	previous_chat = previous_chat + bot

	answer = ai.generate_one(prompt=previous_chat, max_length=len(previous_chat) + 50)
	answer = answer[len(previous_chat):].split("\n")[0]
	if len(answer.split(".")) > 1:
		answer = ".".join(answer.split(".")[:-1])

	return answer
