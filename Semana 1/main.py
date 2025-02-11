import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel("questions.xlsx")
questions = df.sample(n=5).values.tolist()

window = tk.Tk()
window.title("Snoopy: quiz")
window.geometry("400x450")

#colors
background_color = "#030202"
text_color = "#f4f5f6"
button_color = "#137751"
button_text_color = "#FFFFFF"

window.config(bg = background_color)
window.option_add("*Font", "Arial")

#logo
app_icon = PhotoImage(file = "logo.png")
app_label = tk.Label(window, image = app_icon, bg = background_color)
app_label.pack(pady = 10)

#components
questions_label = tk.Label(window, text="Pergunta", wraplength=380, bg = background_color, fg = text_color, font = ("Arial", 12, "bold"))
questions_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(window, text ="", width=30, bg = button_color, fg = button_text_color, state= tk.DISABLED, font = ("Arial", 10, "bold"))
option1_btn.pack(pady = 10)

option2_btn = tk.Button(window, text ="", width=30, bg = button_color, fg = button_text_color, state= tk.DISABLED, font = ("Arial", 10, "bold"))
option2_btn.pack(pady = 10)

option3_btn = tk.Button(window, text ="", width=30, bg = button_color, fg = button_text_color, state= tk.DISABLED, font = ("Arial", 10, "bold"))
option2_btn.pack(pady = 10)

option4_btn = tk.Button(window, text ="", width=30, bg = button_color, fg = button_text_color, state= tk.DISABLED, font = ("Arial", 10, "bold"))
option4_btn.pack(pady = 10)

play_again_btn = tk.Button(window, text ="Jogar novamente", width=30, bg = button_color, fg = button_text_color, font = ("Arial", 10, "bold"))
play_again_btn.pack(pady = 10)

window.mainloop()