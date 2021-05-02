s = input()
lower = []
upper = []
odd = []
even = []
for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            upper.append(s[i])
        else:
            lower.append(s[i])
    else:
        if int(s[i])%2==0:
            even.append(s[i])
        else:
            odd.append(s[i])
lower.sort(), upper.sort(), odd.sort(), even.sort()
print("".join(lower+upper+odd+even))
