# The game() function in a program lets a user play a game and returns-
# the score as an integer. You need to read a file 'HighScore.txt' which-
# is either blank or contains the previous High-Score. You need to write-
# a program to update the High-Score whenever game() breaks the High-Score.

def game():
    return 164

Score = game()
with open("HighScore.txt") as f:
    highScoreStr = int(f.read())

if highScoreStr=='':
    with open("HighScore.txt", "w") as f:
        f.write(str(Score))

elif int(highScoreStr)<Score:
    with open("HighScore.txt", "w") as f:
        f.write(str(Score))