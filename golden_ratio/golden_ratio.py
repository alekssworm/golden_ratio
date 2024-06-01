import turtle

def draw_golden_ratio(iterations=50, initial_length=200):
 
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(1)  # Устанавливаем медленную скорость для черепахи
    t.pensize(3)
    t.color("yellow")

    # Золотое сечение
    phi = (1 + 5 ** 0.5) / 2

    # Начальные значения длин отрезков
    a = initial_length
    b = a / phi

    # Рисуем отрезки золотого сечения
    for _ in range(iterations):
        t.forward(a)
        t.left(90)
        t.circle(b, 180)  # Изогнутая линия вместо прямой
        t.left(90)

        # Обновляем значения для следующего отрезка
        a, b = b, a / phi

    # Закрываем окно по клику
    screen.exitonclick()

draw_golden_ratio(iterations=250, initial_length=200)
