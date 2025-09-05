import tkinter as Calculator

field_text = ""

def add_to_field(sth):
    global field_text
    field_text = field_text + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

def calculate():
    global field_text
    try:
        result = str(eval(field_text))
        field.delete("1.0", "end")
        field.insert("1.0", result)
        field_text = result
    except Exception:
        field.delete("1.0", "end")
        field.insert("1.0", "Error")
        field_text = ""

def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")

# Main window
window = Calculator.Tk()
window.geometry("500x650")
window.config(background="#7393B3")

# Frame centered
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Heading Label (outside frame, top center)
heading = Calculator.Label(window, text="Calculator",
                           font=("Times New Roman", 28, "bold"),
                           bg="#7393B3", fg="#4B0AE3")
heading.grid(row=0, column=1, pady=40)

# Create a frame in the center
frame = Calculator.Frame(window, bg="#9b59b6")
frame.grid(row=1, column=1)

# Entry field (inside frame)
field = Calculator.Text(frame, height=2, width=34, font=("Times New Roman", 20))
field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons (inside frame)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    (".", 4, 0), ("0", 4, 1), ("(", 4, 2), (")", 4, 3),
]

for (text, r, c) in buttons:
    b = Calculator.Button(frame, text=text, command=lambda t=text: add_to_field(t),
                          width=10, height=2, font=("Times New Roman", 14), bg="#e0e0e0")
    b.grid(row=r, column=c, padx=5, pady=5)

# Special last row
btn_clear = Calculator.Button(frame, text="Clear", command=clear,
                              width=10, height=2, font=("Times New Roman", 14), bg="#e0e0e0")
btn_clear.grid(row=5, column=0, padx=5, pady=5)

btn_plus = Calculator.Button(frame, text="+", command=lambda: add_to_field("+"),
                             width=10, height=2, font=("Times New Roman", 14), bg="#e0e0e0")
btn_plus.grid(row=5, column=1, padx=5, pady=5)

btn_equals = Calculator.Button(frame, text="=", command=calculate,
                               width=22, height=2, font=("Times New Roman", 14), bg="#e0e0e0")
btn_equals.grid(row=5, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

window.mainloop()
