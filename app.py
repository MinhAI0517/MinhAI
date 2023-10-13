#Khai báo API key và mô hình 
import openai
openai.api_key = 'API key của bạn' #Thay API key của bạn vào đây
messages = [{'role': 'system', 'content': 'Bạn là một người cực kì thông minh'}]
#Bắt đầu trình chạy
while True:
    cauhoi = input('Bạn: ')  # Nơi bạn nhập câu hỏi
    if cauhoi:
        messages.append({'role': 'user', 'content': cauhoi})
        chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0.5,     # Quyết định độ sáng tạo của chatbot
            max_tokens=50        # Độ dài tối đa của phản hồi (Độ dài của Tiếng Việt khác Tiếng Anh)
        )

        phanhoi = chat.choices[0].message['content']
        print(f'ChatGPT: {phanhoi}') #In ra phản hồi
        messages.append({'role': 'assistant', 'content': phanhoi})
