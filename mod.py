def is_even(n):
    return n % 2 == 0

def evens(numbers):
    res = []
    for n in numbers:
        if is_even(n):
            res.append(n)
    return res

a = evens([2,3,7,9,100,101,134])

print(a)