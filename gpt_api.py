import openai

openai.organization = 'ORGANIZATION_ID_HERE'
openai.api_key = 'API_KEY_HERE'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)
