class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def __str__(self):
        return "({0},{1})".format(self.__x, self.__y)
p1 = Point(2, 3)
print(p1)