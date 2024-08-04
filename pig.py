import math
import random
import turtle  # 🐢
from colorsys import hsv_to_rgb

RANDOM_CENTER = 4


def main() -> int:
    turtle.setup(1.0, 1.0)
    turtle.title("爱心射线")
    turtle.bgcolor("black")

    t = turtle.Turtle()
    t.screen.delay(0)
    t.hideturtle()

    i = 0
    while True:
        try:
            angle = i * (math.sqrt(5) - 1) * math.pi
            color = get_random_pink_color()

            t.color(color)
            t.goto(draw_x(angle) * 20, draw_y(angle) * 20)
            t.goto(
                draw_x(random.random() * 2 * math.pi) * RANDOM_CENTER * random.random(),
                draw_y(random.random() * 2 * math.pi) * RANDOM_CENTER * random.random(),
            )

            i += 1

            if i % 100 == 0:
                print(f"Lines drawn: {i}", end="\r")

        except KeyboardInterrupt:
            break

    print(f"Total Lines drawn: {i}")

    turtle.done()

    return 0


def get_random_pink_color() -> tuple:
    hue = (310 + 25 * random.random()) / 360
    sat = (40 + 30 * random.random()) / 100
    val = (75 + 20 * random.random()) / 100

    return hsv_to_rgb(hue, sat, val)


def draw_x(k):
    return 15 * math.sin(k) ** 3


def draw_y(k):
    return (
        12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
    )


if __name__ == "__main__":
    exit(main())
