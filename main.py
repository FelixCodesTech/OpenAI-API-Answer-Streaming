for i in range(25):
    print("")


import openai
import os

openai.api_key_path = "key.txt"

prompt = input("Input: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Assistant acts like a super funny mexican guy. Assistant speaks english. He mimics all of those classic mexican accents though. He's very nice and amusing to talk to.\n\nHuman: {prompt}\nAssistant:",
  temperature=0.7,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["Human:", "\n"],
  stream=True
)

print(response)

entireResponse = ""

for token in response:
    os.system('cls' if os.name == 'nt' else 'clear')
    entireResponse = f"{entireResponse}{token.choices[0].text}"
    print(entireResponse)