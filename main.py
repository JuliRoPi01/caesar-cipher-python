import tkinter as tk
from tkinter import messagebox


ABC = "abcdefghijklmnopqrstuvwxyz"
FONT = ("comfortaa", 14)


def main() -> None:

    def get_shift() -> int | None:
        usr_shift: str = shift_entry.get()
        if not usr_shift:
            messagebox.showerror("Error", "Enter a shift value")
        elif usr_shift.isdigit():
            return int(usr_shift)
        else:
            messagebox.showerror("Error", "Shift must be a positive integer")

    def code_message() -> None:
        shift: int|None = get_shift()
        if shift == None:
            return
        message: str = message_entry.get()
        code = caesar_cipher(message= message, shift= shift)
        result_label.config(text= code) 

    root = tk.Tk()
    root.title("Caesar Cipher")
    root.config(padx= 20, pady= 20)

    message_entry = tk.Entry(font= FONT)
    message_entry.insert(0, "Message")
    message_entry.grid(row= 0, column= 0)

    shift_entry = tk.Entry(font=FONT)
    shift_entry.grid(row= 0, column=1)

    convert_btn = tk.Button(text= "Convert", command=code_message, font= FONT)
    convert_btn.grid(row= 1, column= 0)

    result_label = tk.Label(text="", font=FONT)
    result_label.grid(row= 1, column= 1)

    root.mainloop()

def caesar_cipher(message, shift) -> str:
    code: str = ""
    for char in message:
        if char.lower() in ABC:
            char_num: int = ABC.index(char.lower())
            new_char_num: int = (char_num+shift)%26
            new_char: str = ABC[new_char_num]

            if char != char.lower():
                new_char = new_char.upper()

            code += new_char

        else:
            code += char
    return code

if __name__  == "__main__":
    main()