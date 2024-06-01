import turtle

def draw_golden_ratio(iterations=50, initial_length=200):
 
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(1)  # ������������� ��������� �������� ��� ��������
    t.pensize(3)
    t.color("yellow")

    # ������� �������
    phi = (1 + 5 ** 0.5) / 2

    # ��������� �������� ���� ��������
    a = initial_length
    b = a / phi

    # ������ ������� �������� �������
    for _ in range(iterations):
        t.forward(a)
        t.left(90)
        t.circle(b, 180)  # ��������� ����� ������ ������
        t.left(90)

        # ��������� �������� ��� ���������� �������
        a, b = b, a / phi

    # ��������� ���� �� �����
    screen.exitonclick()

draw_golden_ratio(iterations=250, initial_length=200)
