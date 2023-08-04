from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.setposition(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 16, 'normal'))

    def add_point(self):
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Arial', 20, 'normal'))