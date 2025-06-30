ABC = "abcdefghijklmnopqrstuvwxyz"

def main() -> None:
    message: str = ask_message()
    shift: int = ask_shift()
    code: str = encode_message(message, shift)
    print(code)

def ask_message() -> str:
    usr_message: str = input("Message to encode: ")
    return usr_message

def ask_shift() -> int:
    while True:
        usr_shift: str = input("Shift number: ")
        if usr_shift.isdigit():
            shift: int = int(usr_shift)
            if shift >= 0:
                return shift
            else:
                print("Number must be positive")
        else:
            print("Shift must be a number")

def encode_message(message, shift) -> str:
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