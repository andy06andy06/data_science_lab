def draw_grid(m, n):
    while m > 0:
        if n > 0:
            print('+ - - '*n + '+')
            print('/     '*n + '/')
            print('/     '*n + '/')
        m-=1
    print('+ - - '*n + '+')

draw_grid(2,3)
