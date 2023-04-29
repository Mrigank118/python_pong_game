from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, 260)
        self.pencolor("white")
        self.ht()
        self.count_l = 0
        self.count_r = 0

    def update(self):
        self.write(f"{self.count_l} : {self.count_r}", align=ALIGNMENT, font=FONT)

    def increase_score_r(self):
        self.count_r += 1
        self.clear()
        self.update()

    def increase_score_l(self):
        self.count_l += 1
        self.clear()
        self.update()

    def gameover(self):
        self.clear()
        self.goto(0, 0)
        if self.count_l > self.count_r:
            self.write("Game Over! Left Won", align=ALIGNMENT, font=FONT)
        elif self.count_l < self.count_r:
            self.write("Game Over! Right Won", align=ALIGNMENT, font=FONT)
        else:
            self.write("Game Over! Draw", align=ALIGNMENT, font=FONT)
