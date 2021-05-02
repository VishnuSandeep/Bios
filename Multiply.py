def multiply(n) :
    result = 1
    for x in n:
         result = result * x
    return result

n = list(map(int,input().strip().split()))
print(multiply(n))
