import timeit

SetInit = 'it = set(range(10000000))'
ListInit = 'it = list(range(10000000))'
Existence = '(n*100 in it for n in range(100000))'

if __name__ == '__main__':
    print('init Set takes {} ms.'.format(
        timeit.timeit(SetInit,number=10)*1000
    ))
    print('find element in Set takes {} ms.'.format(
        timeit.Timer(Existence, setup=SetInit).timeit(number=1000)*1000
    ))
    print('init List takes {} ms.'.format(
        timeit.timeit(ListInit,number=10)
    ))
    print('find element in List takes {} ms.'.format(
        timeit.Timer(Existence, setup=SetInit).timeit(number=1000)*1000
    ))
