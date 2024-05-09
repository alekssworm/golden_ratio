import turtle

def draw_golden_ratio(iterations=10, initial_length=200):
    # ������� ����� � ��������
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # ������������� ������������ �������� ��� ��������

    # ������� �������
    phi = (1 + 5 ** 0.5) / 2

    # ��������� �������� ���� ��������
    a = initial_length
    b = a / phi

    # ������ ������� �������� �������
    for _ in range(iterations):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)

        # ��������� �������� ��� ���������� �������
        a, b = b, a / phi

    # ��������� ���� �� �����
    screen.exitonclick()

draw_golden_ratio(iterations=15, initial_length=200)
