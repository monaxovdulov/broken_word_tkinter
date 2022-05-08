import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [ "магазин", "пальма", "море", "крабы", "корабль"
]

words = []

for word in answers:
    word_list = list(word)
    broken_word = []
    for i in word:
        random_letter = random.choice(word_list)
        broken_word.append(random_letter)
        random_index = word_list.index(random_letter)
        word_list.pop(random_index)
    broken_word = "".join(broken_word)

    words.append(broken_word)
    
    

print(words)
            
