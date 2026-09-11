#this code tested on google colab 
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
print(os.listdir())
model_path = str(input("\n Enter the model path>>> "))

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
max_token = int(input("Enter the max token length>>> "))
breakOut = input("do you want to have breakpoint (y/n)")
while True:
    prompt = input("ask>>")

    inputs = tokenizer(prompt, return_tensors="pt")
    os.system("clear")
    outputs = model.generate(**inputs, max_new_tokens=max_token)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(response)
    if breakOut == "y":
      status = input("do you want to continue (y/n)")
      if status == "y":
        continue
      else:
        break
    else:
       continue