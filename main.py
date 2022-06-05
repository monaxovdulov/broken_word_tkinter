from tkinter import *
import random

# from tkinter import messagebox

answers = [
    "магазин",  # индекс 0
    "пальма",  # индекс 1
    "море",  # индекс 2
    "крабы",  # индекс 3
    "корабль"  # индекс 4
]

words = []  # создаем пустой список

# на первой итерации word = "магазин"
for word in answers:  # цикл фор перебирает элементы списка answers
    word_list = list(word)  # list(word)- создает из строки word список ['м', 'а', 'г', 'а', 'з', 'и', 'н']
    # например если в word была строка 'море' то функция list(word)
    # вернёт список ['м','о','р','е']

    broken_word = []  # создаем пустой список

    # цикл внутри цикла
    for i in word:  # цикл фор перебирает символы строки word
        random_letter = random.choice(word_list)  # выбираем из списка word_list (список с буквами) случайную букву
        # и связываем с переменной random_letter

        broken_word.append(random_letter)  # добавляем в список broken_word случайную букву random_letter
        random_index = word_list.index(random_letter)  # получаем индекс значения random_letter в списке word_list

        word_list.pop(random_index)  # удаляем из списка word_list элемент под индексом random_index
    broken_word = "".join(broken_word)  # создаем из списка с буквами broken_word строку

    words.append(broken_word)  # добавляем эту строку в список words

random_num = random.randint(0, len(words))  # генерирует случайное число,


# по которому мы будем обращаться к списку слов


def show_broken_word():
    broken_word_label['text'] = words[random_num]


def checking_word():
    print("Проверяю слово")
    user_answer = user_answer_entry.get()
    print("Твой ответ", user_answer)
    if user_answer == answers[random_num]:
        print("Ты отгадал слово")
    else:
        print("Ты не отгадал")


# print(num)
print('список answers', answers)
print('список words', words)

root = Tk()  # создаем главное окно
root.geometry("350x400+400+300")
root.title("❤ Почини слово:с ❤")
root.configure(background="#000000")

broken_word_label = Label(
    root,
    text="",
    font=("Verdana", 18),
    bg="#000000",
    fg="#FFFFFF",
)

broken_word_label.pack(pady=30, ipady=10, ipadx=10)

ans1 = StringVar()
user_answer_entry = Entry(
    root,
    font=("Verdana", 16),
    textvariable=ans1,
)
user_answer_entry.pack(ipady=5, ipadx=5)

btn_check = Button(
    root,
    text="Проверить",
    font=("Comic sans ms", 16),
    width=16,
    bg="#4c4b4b",
    fg="#6ab04c",
    relief=GROOVE,
    command=checking_word

)
btn_check.pack(pady=40)

btnreset = Button(
    root,
    text="Начать заново",
    font=("Comic sans ms", 16),
    width=16,
    bg="#4c4b4b",
    fg="#EA425C",
    relief=GROOVE,

)
btnreset.pack()

show_broken_word()

root.mainloop()  # главный Цикл обработки событий
