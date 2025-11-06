def reverse_numbers():
    numbers = []
    for i in range(1,11):
        numbers.append(str(i))
    print(",".join(numbers[::-1]))
    
reverse_numbers()