from curses.ascii import isdigit


def main():
    line = "13zls3"

    decimalconversion = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for name, num in decimalconversion.items():
        line = line.replace(f"{name}", f"{name}{num}{name}")
    print(line)


if __name__ == "__main__":
    main()
