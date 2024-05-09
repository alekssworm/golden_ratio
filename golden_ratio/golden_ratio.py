import turtle

def draw_golden_ratio(iterations=10, initial_length=200):
    # Создаем экран и черепаху
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Устанавливаем максимальную скорость для черепахи

    # Золотое сечение
    phi = (1 + 5 ** 0.5) / 2

    # Начальные значения длин отрезков
    a = initial_length
    b = a / phi

    # Рисуем отрезки золотого сечения
    for _ in range(iterations):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)

        # Обновляем значения для следующего отрезка
        a, b = b, a / phi

    # Закрываем окно по клику
    screen.exitonclick()

draw_golden_ratio(iterations=15, initial_length=200)
