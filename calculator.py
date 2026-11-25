import tkinter as tk

def click(val):
    e.insert(tk.END, val)

def clear():
    e.delete(0, tk.END)

def equal():
    try:
        result = eval(e.get())
        e.delete(0, tk.END)
        e.insert(0, str(result))
    except:
        e.delete(0, tk.END)
        e.insert(0, "Error")

root = tk.Tk()
root.title("Ayesha's Calculator")
root.geometry("300x400")
root.configure(bg="#2b2b2b")

e = tk.Entry(root, font=("Arial", 24), justify="right", bg="white")
e.pack(fill="x", padx=10, pady=10)

buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"]
]

for row in buttons:
    f = tk.Frame(root, bg="#2b2b2b")
    f.pack()
    for b in row:
        if b == "=":
            btn = tk.Button(f, text=b, width=5, height=2, bg="#ff9500", fg="white", font=("Arial", 16), command=equal)
        else:
            btn = tk.Button(f, text=b, width=5, height=2, bg="#4d4d4d", fg="white", font=("Arial", 16), command=lambda x=b: click(x))
        btn.pack(side="left", padx=3, pady=3)

clear_btn = tk.Button(root, text="Clear", width=20, height=2, bg="red", fg="white", font=("Arial", 14), command=clear)
clear_btn.pack(pady=10)

root.mainloop()
