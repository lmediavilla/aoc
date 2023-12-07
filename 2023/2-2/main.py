from re import sub


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
        thisgame = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for ball in balls:
            ball = ball.replace(" ", "")
            if "blue" in ball:
                ball = ball.rstrip("blue")
                thisgame["blue"] = int(ball)
            elif "red" in ball:
                ball = ball.rstrip("red")
                thisgame["red"] = int(ball)
            elif "green" in ball:
                ball = ball.rstrip("green")
                thisgame["green"] = int(ball)
        if thisgame["red"] > mygame["red"]:
            mygame["red"] = thisgame["red"]
        if thisgame["blue"] > mygame["blue"]:
            mygame["blue"] = thisgame["blue"]
        if thisgame["green"] > mygame["green"]:
            mygame["green"] = thisgame["green"]
        else:
            continue
    return mygame["red"] * mygame["blue"] * mygame["green"]


if __name__ == "__main__":
    main()
