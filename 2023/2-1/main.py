from re import sub
myballs = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main():

    sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            sum = sum + gamepossible(line)
    print(sum)


def gamepossible(line):
    mygame = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    line = line.rstrip('\n')
    # Game number
    end = line.index(":")
    start = 4
    gamenumber = int(line[start:end])
    line = line[end + 1:]
    # Game possible
    subgames = line.split(";")
    for game in subgames:
        balls = game.split(",")
        for ball in balls:
            ball = ball.replace(" ", "")
            if "blue" in ball:
                ball = ball.rstrip("blue")
                mygame["blue"] = int(ball)
            elif "red" in ball:
                ball = ball.rstrip("red")
                mygame["red"] = int(ball)
            elif "green" in ball:
                ball = ball.rstrip("green")
                mygame["green"] = int(ball)
        if mygame["red"] > myballs["red"]:
            return 0
        elif mygame["blue"] > myballs["blue"]:
            return 0
        elif mygame["green"] > myballs["green"]:
            return 0
        else:
            continue
    return gamenumber


if __name__ == "__main__":
    main()
