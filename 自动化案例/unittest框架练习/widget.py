#coding=utf-8
class Widget:
    def __init__(self,size=(40,40)):
        self.__size=size
    def getsize(self):
        return self.__size
    def resize(self,Widget,height):
        if Widget<0 or height<0:
            raise ValueError("illegal size")
        self.__size=(Widget,height)

    def dispose(self):
        pass