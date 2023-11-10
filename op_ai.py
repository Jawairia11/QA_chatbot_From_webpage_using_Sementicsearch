import openai
openai.api_key = "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"
def chat_bot(question, info):
    chat = openai.chat.completions.create(
        model = "gpt-3.5-turbo" ,
        messages = [
            {"role":"system", "content":"You are an AI assistant how will answer the question of user based on the data provided.If you find the answer return a response that data does not have answer for this question"},

            {
                "role": "user",
                "content": f"""answer the question based on the question, using the information provided
                '''question:{question}'''
                '''information:{info}'''
                """
            }
        ], 

        temperature = 0
    )
    return chat.choices[0].message.content
