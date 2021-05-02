n = list(map(int,input().strip().split()))
for num in n:
    if num<0:
        a = False
    else:
        a = True
    if num not in range(10):
        b = False
    else:
        b = True
    if str(num)== str(num)[::-1]:
        c= True
    else:
        c = False 
if a and (b or c):
    print(True)
else:
    print(False)
