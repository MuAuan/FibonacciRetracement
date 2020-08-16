def calc_fib(n):
    if n ==1 or n== 2:
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)

print('__name__1:', __name__)

if __name__ == '__main__':
    n0=30    
    for n in range(1,n0+1):
        print(calc_fib(n),end=' ')
    print()    
    for n in range(1,n0+1):
        print('{0:.2f}'.format(calc_fib(n)/calc_fib(n0)*100),end=' ')

