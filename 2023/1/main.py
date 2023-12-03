import os


def main():
    sum = 0
    file = open("input.txt", "r")
    try:
        for line in file:
            result, number = twonumbers(line)
            if True == result:
                sum += number
            else:
                continue
        print(sum)
    except BaseException:
        print("Exception found")
    finally:
        file.close()


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
        return True, number
    elif counter == 1:
        strnumber = str(numvec[0]) + str(numvec[0])
        number = int(strnumber)
        return True, number
    else:
        return False, 0


if __name__ == "__main__":
    main()
