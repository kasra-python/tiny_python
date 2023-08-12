fibo = [0,1] 
n = int(input('your range number is 0 - :'))
fibo_func = lambda x:x.append(x[-1]+x[-2])

for i in range(0,n+1):
    fibo_func(fibo)
    if fibo[-1] > n:
        fibo.pop()
        break
print(f"The fibonacci sequence in range of 0-{n} is {fibo}")
