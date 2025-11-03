from turtle import *
screensize(3500, 3500)
m = 30
tracer(0)
rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)
up()
for x in range(-17,1):
    for y in range(0, 7):
        goto(x * m, y * m)
        dot(3,'blue')
update()
done()

# 30