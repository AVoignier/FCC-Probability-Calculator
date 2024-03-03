import copy
import random

class Hat:
    def __init__(self, **kwargs):
        print("test")
        self.contents = []
        for key, value in kwargs.items():
            for i in range(0, value):
                self.contents.append(key)

        print(self.contents)

    def draw(self, nb_balls):
        if nb_balls >= len(self.contents):
            return self.contents

        contents_copy = self.contents[:]
        str_balls = ""
        removed_balls = []
        for i in range(0,nb_balls):
            rand_index = random.randrange(len(contents_copy))
            removed_balls.append( contents_copy.pop(rand_index) )
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    nb_experiments_ok = 0

    for _ in range(num_experiments):
        draw_ball = hat.draw(num_balls_drawn)

        draw_ok = True
        for ball_color, nb_ball_expected in expected_balls.items():
            if len( [ball for ball in draw_ball if ball == ball_color ] ) < nb_ball_expected:
                draw_ok = False
        
        print(draw_ball, expected_balls, draw_ok)
        
        if draw_ok:
            nb_experiments_ok += 1

    return nb_experiments_ok/num_experiments

if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
        expected_balls={"red":2,"green":1},
        num_balls_drawn=5,
        num_experiments=2000)
    print(probability)