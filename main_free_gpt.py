# pip install -U g4f

import g4f
from datetime import datetime

g4f.logging = True  # enable logging
g4f.check_version = False  # Disable automatic version checking
print(g4f.version)  # check version
print(g4f.Provider.Ails.params)  # supported args


# Automatic selection of provider

def write_to_txt(text_str):
    with open('history.txt', 'a') as txt_file:
        txt_file.write(text_str)


def receive_answer(question):
    write_to_txt(f'\n\n\n___{datetime.now().strftime("%d.%m.%Y")}___\n-----вопрос-----\n{question}\n\n')
    # streamed completion
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    return response


if __name__ == '__main__':
    response = receive_answer(input("enter question\n\n"))
    for message in response:
        print(message, end='')

        write_to_txt(message)
