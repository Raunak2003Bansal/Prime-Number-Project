def prime(n):
    if n<=1:
        return "Pls enter a number greater than or equal to 2"
    else:
        for i in range(2,n,1):
            if n%i==0:
                return f"{n} is not a Prime Number"
        return f"{n} is a Prime Number"