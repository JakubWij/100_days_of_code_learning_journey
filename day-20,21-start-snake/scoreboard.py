from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
