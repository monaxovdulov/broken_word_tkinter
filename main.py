
from tkinter import *
import random
from tkinter import messagebox

answers = [ "магазин", "пальма", "море", "крабы", "корабль"
]

words = [] # создаем пустой список

# word = "магазин" 
for word in answers: # цикл фор перебирает элементы списка answers
    word_list = list(word)# list(word)- создает из строки word список
    # например если в word была строка 'море' то функция list(word)
    # вернёт список ['м','о','р','е']
    
    broken_word = [] # создаем пустой список
    
    # цикл внутри цикла
    for i in word: # цикл фор перебирает символы строки word
        random_letter = random.choice(word_list)# выбираем из списка word_list (список с буквами) случайную букву
        # и связываем с переменной random_letter
        
        broken_word.append(random_letter) # добавляем в список broken_word случайную букву random_letter
        random_index = word_list.index(random_letter)# получаем индекс значения random_letter в списке word_list
        
        word_list.pop(random_index) # удаляем из списка word_list элемент под индексом random_index
    broken_word = "".join(broken_word) # создаем из списка с буквами broken_word строку 

    words.append(broken_word)# добавляем эту строку в список words
    

num = random.randrange(0, len(words), 1)
print(num)


print(words)

root = Tk()
root.geometry("350x400+400+300")
root.title("Broken word❤")
root.configure(background="#000000")

lbl = Label(
    root,
    text="Your here",
    font=("Verdana", 18),
    bg="#000000",
    fg="#FFFFFF",
)

lbl.pack(pady=30, ipady=10, ipadx=10)

ans1 = StringVar()
e1 = Entry(
    root,
    font=("Verdana", 16),
    textvariable=ans1,
)
e1.pack(ipady=5, ipadx=5)


btncheck = Button(
    root,
    text="Check",
    font=("Comic sans ms", 16),
    width=16,
    bg="#4c4b4b",
    fg="#6ab04c",
    relief=GROOVE,
    
)
btncheck.pack(pady=40)


btnreset = Button(
    root,
    text="Reset",
    font=("Comic sans ms", 16),
    width=16,
    bg="#4c4b4b",
    fg="#EA425C",
    relief=GROOVE,

)
btnreset.pack()





root.mainloop()






