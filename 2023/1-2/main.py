import os
from curses.ascii import isdigit


def main():
    sum = 0
    try:
        file = open("input.txt", "r")
        for line in file:
            newline = stringtonumbers(line)
            number = twonumbers(newline)
            print(f"{line} - {newline} - {number}")
            sum += number
    except BaseException:
        print("Exception found")
    finally:
        file.close()
    print(sum)


def stringtonumbers(line):
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
    return line


def twonumbers(line):
    counter = 0
    numvec = []
    for c in line:
        if (c.isdigit()):
            counter += 1
            numvec.append(int(c))
        else:
            continue
    if counter >= 2:
        strnumber = str(numvec[0]) + str(numvec[len(numvec) - 1])
        number = int(strnumber)
        return number
    elif counter == 1:
        strnumber = str(numvec[0]) + str(numvec[0])
        number = int(strnumber)
        return number
    else:
        return 0


if __name__ == "__main__":
    main()
