'''
Make a maximum number by using operators(+, -, /, *).
The each number get from input string.
The each number should be from 0 to 9.
eg. 
input       result
567         5*6*7 = 210
0291         0+2*9+1 = 19
'''
data = input()

return = int(data[0])

for i in range(1, len(data)):
    # If one of them is '0' or '1', use '+' instead of '*'.
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
