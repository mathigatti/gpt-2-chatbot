from aitextgen import aitextgen

human = "The man said, "
bot = "God said, "
full_chat = f"{human}Is heaven a good place?\n{bot}The Bible says so.\n{human}Then it must be true my lord.\n{bot}Yes, these are my words son.\n"

def start_model():
	ai = aitextgen(model="aitextgen/pytorch_model_355M.bin", config="aitextgen/config_355M.json", to_gpu=True)
	return ai

ai = start_model()

def answer(ai,previous_chat):
	previous_chat = "\n".join(previous_chat.split("\n")[-12:]) + "\n"
	previous_chat = previous_chat + bot

	answer = ai.generate_one(prompt=previous_chat, max_length=50)
	answer = answer[len(previous_chat):].split("\n")[0]
	if len(answer.split(".")) > 1:
		answer = ".".join(answer.split(".")[:-1])

	if len(answer) < 2:
		return "*NO ANSWER*"

	return answer
