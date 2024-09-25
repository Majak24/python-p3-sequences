def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return
    
    fib_sequence = [0]
    if length > 1:
        fib_sequence.append(1)
    
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    print(fib_sequence)

# Test cases
print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)