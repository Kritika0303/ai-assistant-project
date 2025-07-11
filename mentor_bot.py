import openai
client = openai.OpenAI(api_key = "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")

def ask_chatgpt(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding mentor who explains code and helps debug."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Keep asking questions in a loop
while True:
    user_input = input("Ask your AI mentor (type 'exit' to quit): ")
    if user_input.lower() in ["exit", "quit"]:
        break
    answer = ask_chatgpt(user_input)
    print("\nAI Mentor:", answer, "\n")
