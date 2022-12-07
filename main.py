# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as turtle_module
import random


tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(188, 19, 46), (243, 232, 66), (251, 230, 236), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187)]

tim.setheading(225)
tim.fd(250)
tim.setheading(0)
number_of_dots = 101




for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)


    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()


