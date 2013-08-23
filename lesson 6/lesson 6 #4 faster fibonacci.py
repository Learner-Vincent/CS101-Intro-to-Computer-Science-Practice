#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print fibonacci(0)
print fibonacci(1)
print fibonacci(2)

print fibonacci(36)
#>>> 14930352