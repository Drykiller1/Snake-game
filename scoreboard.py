from turtle import *
with open("save.txt", "r") as content:
    high_score = int(content.read())

ALIGNMENT = "center"
FONT = ("Arial",24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = high_score
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def score_board_location(self):
        self.goto(x=-125, y=250)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def highest_score_board_location(self):
        self.goto(x=75, y=250)
        self.write(f"Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def ate_apple(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def keep_score(self, current_score):
        if current_score > self.high_score:
            with open("save.txt", mode="w") as file:
                file.write(str(current_score))