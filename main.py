ABC = "abcdefghijklmnopqrstuvwxyz"

def main() -> None:
    message: str = ask_message()
    activity: str = ask_activity()
    shift: int = ask_shift()

    if activity == "d":
        shift *= -1

    code: str = code_message(message, shift)
    print(f"Code: {code}")

def ask_message() -> str:
    usr_message: str = input("Message to encode/decode: ")
    return usr_message

def ask_activity() -> str:
    while True:
        usr_activity: str = input("Are you going to encode or decode (e or d): ").strip()
        if usr_activity == "e" or usr_activity == "d":
            return usr_activity
        print("Write 'e' to encode or 'd' to decode")

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

def code_message(message, shift) -> str:
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