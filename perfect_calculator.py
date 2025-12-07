import tkinter as tk
from tkinter import messagebox
import math

PASSWORD = "saro"
history = []
expression = ""

def check_password():
    def verify():
        pwd = password_entry.get()
        if pwd == PASSWORD:
            login.destroy()
            main_calculator()
        else:
            messagebox.showerror("Error", "Wrong Password! Access Denied.")
            login.destroy()

    login = tk.Tk()
    login.title("Password Required")
    login.geometry("360x180")
    login.configure(bg="#f0e6f6")
    login.resizable(False, False)
    tk.Label(login, text="Enter Password:", font=("Comic Sans MS", 14, "bold"), bg="#f0e6f6").pack(pady=15)
    password_entry = tk.Entry(login, show="*", font=("Arial", 14))
    password_entry.pack(pady=5)
    tk.Button(login, text="Submit", font=("Arial", 12, "bold"), bg="#ffb6c1", fg="white", command=verify).pack(pady=15)
    login.mainloop()

def button_click(value):
    global expression
    expression += str(value)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def calculate():
    global expression, history
    try:
        exp = expression.replace("^", "**")
        exp = exp.replace("sin", "math.sin(math.radians")
        exp = exp.replace("cos", "math.cos(math.radians")
        exp = exp.replace("tan", "math.tan(math.radians")
        exp = exp.replace("sqrt", "math.sqrt")
        exp = exp.replace("log", "math.log")
        exp = exp.replace("exp", "math.exp")
        if "math.sin" in exp or "math.cos" in exp or "math.tan" in exp:
            exp += ")" * exp.count("math.")
        result = eval(exp)
        result_fmt = int(result) if result == int(result) else round(result,6)
        input_text.set(result_fmt)
        history.append(f"{expression} = {result_fmt}")
        expression = str(result_fmt)
    except Exception:
        input_text.set("Error")
        expression = ""

def show_history():
    if not history:
        messagebox.showinfo("History", "No calculations yet.")
        return
    h = "\n".join(history)
    messagebox.showinfo("History", h)

def create_button(frame, text, row, col, width=6, height=3, bg="#e0e0e0", fg="black", command=None):
    btn = tk.Button(frame, text=text, width=width, height=height, bg=bg, fg=fg,
                    font=("Arial", 14, "bold"), relief="raised", command=command)
    btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
    def on_enter(e):
        btn['bg'] = "#ff9999"
    def on_leave(e):
        btn['bg'] = bg
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

def main_calculator():
    global root, input_text
    root = tk.Tk()
    root.title("❤️ Saravanan Calculator ❤️")
    root.geometry("420x620")
    root.configure(bg="#fdf6f0")
    root.resizable(False, False)
    input_text = tk.StringVar()
    input_text.set("")  # initialize properly

    # Input frame
    input_frame = tk.Frame(root, bg="#ffe6f0", bd=3, relief="ridge")
    input_frame.pack(pady=10, padx=10, fill="x")
    input_field = tk.Entry(input_frame, font=('Comic Sans MS', 28, 'bold'),
                           textvariable=input_text, justify='right', bd=0, bg="#fff0f5", fg="#ff1493")
    input_field.pack(ipady=15, fill="x")

    # Buttons frame
    btns_frame = tk.Frame(root, bg="#fdf6f0")
    btns_frame.pack(padx=10, pady=10, fill="both", expand=True)

    for i in range(7):
        btns_frame.rowconfigure(i, weight=1)
    for j in range(4):
        btns_frame.columnconfigure(j, weight=1)

    # Row 1
    create_button(btns_frame, "C", 0, 0, bg="#ffb6c1", command=clear)
    create_button(btns_frame, "←", 0, 1, bg="#ffb6c1", command=backspace)
    create_button(btns_frame, "%", 0, 2, bg="#add8e6", command=lambda: button_click("%"))
    create_button(btns_frame, "/", 0, 3, bg="#add8e6", command=lambda: button_click("/"))

    # Row 2
    create_button(btns_frame, "7", 1, 0, command=lambda: button_click("7"))
    create_button(btns_frame, "8", 1, 1, command=lambda: button_click("8"))
    create_button(btns_frame, "9", 1, 2, command=lambda: button_click("9"))
    create_button(btns_frame, "*", 1, 3, bg="#add8e6", command=lambda: button_click("*"))

    # Row 3
    create_button(btns_frame, "4", 2, 0, command=lambda: button_click("4"))
    create_button(btns_frame, "5", 2, 1, command=lambda: button_click("5"))
    create_button(btns_frame, "6", 2, 2, command=lambda: button_click("6"))
    create_button(btns_frame, "-", 2, 3, bg="#add8e6", command=lambda: button_click("-"))

    # Row 4
    create_button(btns_frame, "1", 3, 0, command=lambda: button_click("1"))
    create_button(btns_frame, "2", 3, 1, command=lambda: button_click("2"))
    create_button(btns_frame, "3", 3, 2, command=lambda: button_click("3"))
    create_button(btns_frame, "+", 3, 3, bg="#add8e6", command=lambda: button_click("+"))

    # Row 5
    create_button(btns_frame, "0", 4, 0, width=14, command=lambda: button_click("0"))
    create_button(btns_frame, ".", 4, 1, command=lambda: button_click("."))
    create_button(btns_frame, "=", 4, 2, bg="#90ee90", command=calculate)
    create_button(btns_frame, "^", 4, 3, bg="#dda0dd", command=lambda: button_click("^"))

    # Row 6
    create_button(btns_frame, "sin", 5, 0, bg="#dda0dd", command=lambda: button_click("sin"))
    create_button(btns_frame, "cos", 5, 1, bg="#dda0dd", command=lambda: button_click("cos"))
    create_button(btns_frame, "tan", 5, 2, bg="#dda0dd", command=lambda: button_click("tan"))
    create_button(btns_frame, "sqrt", 5, 3, bg="#fafad2", command=lambda: button_click("sqrt"))

    # Row 7
    create_button(btns_frame, "log", 6, 0, bg="#fafad2", command=lambda: button_click("log"))
    create_button(btns_frame, "exp", 6, 1, bg="#fafad2", command=lambda: button_click("exp"))
    create_button(btns_frame, "History", 6, 2, bg="#ffa500", command=show_history)
    create_button(btns_frame, "%", 6, 3, bg="#add8e6", command=lambda: button_click("%"))

    root.mainloop()

check_password()


