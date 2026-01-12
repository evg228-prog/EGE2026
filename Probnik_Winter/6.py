from turtle import *

screensize(3500, 3500)
m = 27
tracer(0)
for i in range(2):
    fd(14 * m)
    lt(270)
    bk(12 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
bk(7 * m)
lt(90)
down()
for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
for x in range(14, 23):
    for y in range(1, 8):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()

# 251