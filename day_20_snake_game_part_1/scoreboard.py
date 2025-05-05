from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over.", move=False, align="center", font=FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.write_score()

