# print Fibonacci sequence

def fib(n):

    a, b = 0, 1
    fib_list = [a]
    for i in range(n-1):
        a, b = b, a+b
        fib_list.append(a)
    print('斐波那契数列第{}个数值是{}'.format(n, a))
    print('该斐波那契数列是' + str(fib_list))


fib(10)