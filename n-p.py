def K(n , p) :
    if n == 1:
        return p 
    else:
        return n*p + K(n-1, p)
    
n=int(input("n: "))
p=int(input("p: "))
print(K(n, p))
