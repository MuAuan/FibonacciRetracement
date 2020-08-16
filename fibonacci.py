def calc_fib(n):
    if n ==1 or n== 2:
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)

def calc_fib3(m): #fastest
    a, b = 1, 1
    for _ in range(m-2):
        a, b = b, a + b
    return b    

def main():
    n0=30    
    for n in range(1,n0+1):
        print(calc_fib3(n),end=' ')
    print()    
    for n in range(1,n0+1):
        print('{0:.30f}'.format(calc_fib3(n)/calc_fib3(n0)*100),end=' ')
    print()    
    for n in range(1,n0+1):
        print('{0:.30f}'.format(calc_fib3(n)/calc_fib3(n0-5)*100),end=' ')    
    

if __name__ == '__main__':
    main()

