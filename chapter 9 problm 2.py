def game():
    return 64

score = game()
with open("high score .txt") as f:
    highscore = int(f.read())

if highscore<score:
    with open ("high score .txt", "w") as f:
        f.write(str(score))