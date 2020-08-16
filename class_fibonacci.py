import numpy as np

class MyFibonacciClass:
    f_const = 0.6180339887498949 #514229/832040 #0.6180
    def __init__(self,x=1,y=0,n=10):
        self.x = x
        self.y = y
        self.n = n
                
    def calc_1(self,n):
        const = 1
        for i in range(1,n):
            const *= MyFibonacciClass.f_const
        return const, self.y + const*(self.x - self.y), self.x - const*(self.x - self.y)
    def calc_1_(self,n):
        const = 1
        for i in range(1,n):
            const *= MyFibonacciClass.f_const
        return self.y + (1-const)*(self.x - self.y)
    
    def calc_fib(self,m, sb1,sb2):
            if m ==1 or m== 2:
                return 1
            else:
                return sb1 + sb2
    def calc_fib2(self,m):
            if m ==1 or m== 2:
                return 1
            else:
                return MyFibonacciClass.calc_fib2(self,m-1) + MyFibonacciClass.calc_fib2(self,m-2)
            
    def calc_fib3(self, m): #fastest
        a, b = 1, 1
        for _ in range(m-2):
            a, b = b, a + b
        return b
    
    def calc_fib4(self,m): # m =< 70
        return round((((1 + 5 ** 0.5) / 2) ** m - ((1 - 5 ** 0.5) / 2) ** m) / 5 ** 0.5)
  
    def calc_print(self):
        sb1 = 1
        sb2 = 1
        for n0 in range(1,self.n+1):
            s = MyFibonacciClass.calc_fib(self,n0, sb1, sb2)
            print(n0, s,end=' ')
            #print(s,end=' ')
            rs = np.float64(sb1/s)
            rs1 = np.float64(s/sb1)
            print(rs, rs1)
            #print('{0:5,.5f}'.format(rs1), end=' ')
            sb2 = sb1
            sb1 = s
            
if __name__ == '__main__':
    fibonacci1 = MyFibonacciClass(1604.5,834.6,10)

    for i in range(1,11,1):
        c,a,b = fibonacci1.calc_1(i)
        print('{0:5,.3f}_{1:5,.3f}_{2:5,.3f}'.format(c,a,b))

    fibonacci2 = MyFibonacciClass(1604.5,834.6,10000)
    fibonacci2.calc_print()

    print(fibonacci2.calc_fib3(1000000))