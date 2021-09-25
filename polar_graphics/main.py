import time

import numpy as np
import turtle


from functions import (
    four_petal_rose,
    three_petal_rose,
    logarithmic_spiral,
    hyperbolic_spiral,
    archimede_spiral,
    cardiode,
)


def draw_graph(
        cursor,
        func,
        a=200,
        angle_step=0.01,
        end_angle_multiplier=2
):
    start_angle = 0.01
    for angle in np.arange(0.01, end_angle_multiplier * np.pi, angle_step):
        r = func(a, angle)
        x, y = r * np.cos(angle), r * np.sin(angle)
        if angle == start_angle:
            cursor.penup()
            cursor.goto(int(x), int(y))
            cursor.pendown()

        cursor.setx(int(x))
        cursor.sety(int(y))


if __name__ == '__main__':
    t = turtle.Turtle()
    t.pen(pencolor='black', fillcolor='orange', pensize=2, speed=80)
    time.sleep(5)
    draw_graph(
        cursor=t,
        func=archimede_spiral,
        a=10,
        angle_step=0.02,
        end_angle_multiplier=10,
    )
    s = turtle.Screen()
    s.mainloop()
