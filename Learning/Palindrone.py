
def is_palindrome(x: int) -> bool:
    temp: int = x
    rem: int = 0
    rep: int  = 0

    while (temp>0):
        rem = temp%10
        rep = (rep*10) + rem
        temp = temp//10 #Using integer conversion
        #print('temp', temp)

    return x==rep


print(is_palindrome(121))

#121%10= 1
#121/10=12

"""
rem:    1       2       1
rep:    1       12      121
temp:   12      2       0


"""