import turtle


def draw_branch(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(45)
    draw_branch(t, branch_length * 0.75, level - 1)

    t.right(90)
    draw_branch(t, branch_length * 0.75, level - 1)

    t.left(45)
    t.backward(branch_length)


def main():
    turtle_screen = turtle.Screen()
    turtle_screen.setup(width=800, height=600)
    t = turtle.Turtle()
    t.speed('fastest')
    t.color("green")
    t.left(90)
    t.penup()
    t.goto(0, -150)
    t.pendown()

    level = int(turtle.textinput("Рівень рекурсії",
                "Введіть рівень рекурсії:") or 7)
    draw_branch(t, 100, level)
    t.hideturtle()
    turtle_screen.mainloop()


if __name__ == "__main__":
    main()
