from turtle import Turtle
import os.path


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.setposition(0, 275)
        self.get_score()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align='center',
                   font=('Arial', 16, 'normal'))

    def get_score(self):
        if os.path.isfile('data.txt'):
            with open('data.txt') as file:
                self.high_score = int(file.read())

    def add_point(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write('GAME OVER', move=False, align='center', font=('Arial', 20, 'normal'))
