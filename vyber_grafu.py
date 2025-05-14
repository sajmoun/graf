import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import math

def vykresli():
    funkce = funkce_var.get()

    try:
        a = float(entry_a.get())
    except:
        messagebox.showerror("Chyba", "Zadej platné číslo pro a")
        return

    try:
        b = float(entry_b.get())
    except:
        messagebox.showerror("Chyba", "Zadej platné číslo pro b")
        return

    c = 0
    if funkce == "Kvadratická":
        try:
            c = float(entry_c.get())
        except:
            messagebox.showerror("Chyba", "Zadej platné číslo pro c")
            return

    x = np.linspace(-10, 10, 400)
    y = None

    try:
        if funkce == "Lineární":
            y = a * x + b
        elif funkce == "Kvadratická":
            y = a * x**2 + b * x + c
        elif funkce == "Exponenciální":
            y = a * np.exp(b * x)
        elif funkce == "Logaritmická":
            x = np.linspace(0.1, 10, 400)
            y = a * np.log(x) / np.log(b)
        else:
            messagebox.showerror("Chyba", "Neznámá funkce.")
            return
    except Exception as e:
        messagebox.showerror("Chyba", f"Výpočet selhal: {e}")
        return

    plt.plot(x, y)
    plt.title(f"{funkce} funkce")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


# GUI
okno = tk.Tk()
okno.title("Graf funkce")

tk.Label(okno, text="Vyber funkci:").pack()
funkce_var = tk.StringVar(value="Lineární")
options = ["Lineární", "Kvadratická", "Exponenciální", "Logaritmická"]
tk.OptionMenu(okno, funkce_var, *options).pack()

tk.Label(okno, text="a:").pack()
entry_a = tk.Entry(okno)
entry_a.pack()

tk.Label(okno, text="b:").pack()
entry_b = tk.Entry(okno)
entry_b.pack()

tk.Label(okno, text="c (pouze pro kvadratickou):").pack()
entry_c = tk.Entry(okno)
entry_c.pack()

tk.Button(okno, text="Vykresli graf", command=vykresli).pack(pady=10)

okno.mainloop()
