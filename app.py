
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



import openai

openai.api_key = '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'

messages = [{'role': 'system', 'content': 'Bạn là một người cực kì thông minh'}]

while True:
    cauhoi = input('Ban: ')  # Nơi bạn nhập câu hỏi
    if cauhoi:
        messages.append({'role': 'user', 'content': cauhoi})
        chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0.5,
            max_tokens=50
        )

        phanhoi = chat.choices[0].message['content']
        print(f'ChatGPT: {phanhoi}')
        messages.append({'role': 'assistant', 'content': phanhoi})
