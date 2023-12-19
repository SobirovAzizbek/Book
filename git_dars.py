# import turtle as sm
# import colorsys
# sm.bgcolor("black")
# sm.tracer(2)
# sm.pensize(2)
# h = 0
#
# for i in range(250):
#     color = colorsys.hsv_to_rgb(h, 0.9, 1)
#     h += 0.006
#     sm.pencolor(color)
#     sm.left(179)
#     sm.backward(i * 0.3)
#     sm.circle(i * 0.3, 120)
#     sm.right(14)
#     sm.forward(i * 0.2)
#     sm.circle(i * .3, 120)
# sm.done


class Book:
    def __init__(self, author, year, name, isbn):
        self.author = author
        self.year = year
        self.name = name
        self.isbn = isbn

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getName(self):
        return self.name

    def getIsbn(self):
        return self.isbn

    def Book_Info(self):
        return f"{self.author}{self.year}{self.name}{self.isbn}"


book = Book("Author:Abdulla Qodiriy\n", f"Year:{1920}", "\nName:O'tgan kunlar\n", f"Isbn:{19102}")
print(book.Book_Info())
