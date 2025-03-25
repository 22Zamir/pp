while True:
    user_id = input('Кто пишет:\n>>>')
    if user_id == '/h':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                for i_message in file:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История пуста\n')
    elif user_id == '/exit':
        break
    else:
        message = input('Введите сообщение:\n>>>')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write(f'{user_id}:{message}\n')
