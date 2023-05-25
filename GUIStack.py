import tkinter as tk

def push():
    global stk
    global top

    value = int(entry.get())
    stk.append(value)
    top += 1
    update_display()

def display():
    global stk

    if not stk:
        stack_text.set("Stack is Empty.")
    else:
        stack_text.set("\n".join(str(item) for item in stk[::-1]))

def peek():
    global stk
    global top

    if not stk:
        stack_text.set("Stack is empty.")
    else:
        stack_text.set("PEEK = " + str(stk[top]))

def pop():
    global stk
    global top

    if not stk:
        stack_text.set("Stack is empty.")
    else:
        stk.pop(top)
        top -= 1
        update_display()

def update_display():
    display()
    entry.delete(0, tk.END)

stk = []
top = -1

window = tk.Tk()
window.title("Stack GUI")
window.configure(bg="#f2f2f2")

stack_label = tk.Label(window, text="Stack:", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333333")
stack_label.pack(pady=10)

stack_text = tk.StringVar()
stack_text.set("")

stack_display = tk.Label(window, textvariable=stack_text, font=("Arial", 14), bg="#f2f2f2", fg="#555555")
stack_display.pack(pady=5)

entry_label = tk.Label(window, text="Enter a number:", font=("Arial", 12), bg="#f2f2f2", fg="#333333")
entry_label.pack()

entry = tk.Entry(window, font=("Arial", 12), width=15, bd=2, relief=tk.GROOVE)
entry.pack(pady=5)

push_button = tk.Button(window, text="Push", font=("Arial", 12, "bold"), bg="#4CAF50", fg="#ffffff", relief=tk.RAISED, bd=2, command=push)
push_button.pack(pady=5)

peek_button = tk.Button(window, text="Peek", font=("Arial", 12, "bold"), bg="#2196F3", fg="#ffffff", relief=tk.RAISED, bd=2, command=peek)
peek_button.pack(pady=5)

pop_button = tk.Button(window, text="Pop", font=("Arial", 12, "bold"), bg="#F44336", fg="#ffffff", relief=tk.RAISED, bd=2, command=pop)
pop_button.pack(pady=5)

window.mainloop()
