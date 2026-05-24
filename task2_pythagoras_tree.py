import turtle
import math


def draw_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(45)
    draw_tree(t, branch_length * 0.7, level - 1)

    t.right(90)
    draw_tree(t, branch_length * 0.7, level - 1)

    t.left(45)
    t.backward(branch_length)


def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_tree(t, 120, level)

    screen.mainloop()


if __name__ == "__main__":
    main()