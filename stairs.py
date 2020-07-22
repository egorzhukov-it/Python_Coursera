import sys
num_steps = int(sys.argv[1])

for i in range(1, num_steps+1):
    a = " "*(num_steps-i)
    b = "#"*i
    print(a+b)