from turtle import *
screensize(3500,3500)
m = 10
tracer(0)
for i in range(2):
    fd(23 * m)
    lt(90)
    bk(27 * m)
    lt(90)
up()
bk(5 * m)
rt(90)
fd(11 * m)
lt(90)
down()
for i in range(2):
    fd(26 * m)
    rt(90)
    fd(32 * m)
    rt(90)
up()
for x in range(-5, 24):
    for y in range(-43, 1):
        goto(x * m, y * m)
        dot(3,'blue')
update()
done()

