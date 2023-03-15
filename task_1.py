import time


def sum_to_num(num):
    """
    Use the formula for an arithmetic progression to calculate the sum of all numbers from 1 to n.
    sum = ((a_1+a_n)*n)/2
    a_1 = 1
    a_n = num
    n = num
    """
    return (num * (num + 1)) // 2


n = int(input("Enter number: "))
result = sum_to_num(n)
print(f"The sum of numbers from 1 to {n} is {result}.")
