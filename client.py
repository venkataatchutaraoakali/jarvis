from openai import OpenAI
client = OpenAI(
    api_keys="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",

)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful  virtual assistant naed jarvis skilled in general tasks lie alexa and google cloud"},
        {
            "role": "user","content": "what is coding ." }
    ]
)

print(completion.choices[0].message.content)
