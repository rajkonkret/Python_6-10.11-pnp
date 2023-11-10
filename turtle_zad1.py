import turtle

# turtle - rysowanie zółwiem

wm = turtle.Screen()
wm.title("Moj pierwszy program z Turtle")

pen = turtle.Turtle()

for i in range(4):
    pen.forward(100)
    pen.right(90)

wm.mainloop()
# pip freeze > requirements.txt
# pip install -r requirements.txt
