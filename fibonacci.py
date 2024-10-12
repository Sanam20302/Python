def fibonacci_2(num):
    if num <= 1:
        return num
    else:
        return fibonacci_2(num-1) + fibonacci_2(num-2)    # Using Recursion

def print_fibonacci_series(num):
    for i in range(num):
        print(fibonacci_2(i), end=' ')

def fibonacci_1(num):
    a,b=0,1
    print(a,end=" ")
    for i in range(num-1):                                 # Without using Recursion
        a,b=b,a+b
        print(a,end=" ")
    print()

num = int(input("Enter the number : "))
fibonacci_1()(num)
print_fibonacci_series(num)
