#coding=utf-8
#元类的基础,定义一个说什么的返回什么的元类函数
class SayMetaClass(type):
    def __new__(cls, name, bases,attrs):
        attrs['say_'+name]=lambda self,valus,saying=name:print(saying+','+valus+'!')
        return type.__new__(cls,name,bases,attrs)



#一而二，创建类
class Hello(object,metaclass=SayMetaClass):
    pass
#生成实例
hello=Hello()
#调用元类的方法
hello.say_Hello("world")


