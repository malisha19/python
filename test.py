# def foo():
#     pass


# def bar():
#     pass


# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()
def foo():
    b = 'hello'#局部变量属于局部作用域，在foo函数的外部并不能访问到它；但对于foo函数内部的bar函数来说，变量b属于嵌套作用域，在bar函数中我们是可以访问到它的

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100 #全局变量
    # print(b)  # NameError: name 'b' is not defined
    foo()
#

def foo():
    a = 200 #局部变量
    print(a)  # 200


if __name__ == '__main__':
    a = 100 #全局变量
    foo()
    print(a)  # 100

#如果我们希望在foo函数中修改全局作用域中的a，代码如下所示。
def foo():
    global a #把局部变量改成了全局变量
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200