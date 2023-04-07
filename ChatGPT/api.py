import openai
openai.api_key = "Your_API"

prompt= input("What are you looking for?: ")

response = openai.Completion.create(engine="text-davinci-003",prompt=prompt
        ,max_tokens=1024)
print(response["choices"][0]["text"])
