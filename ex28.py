def make_number(end, step):
    i = 0
    numbers = []
    for num in range(0, end, step):

        numbers.append(i)
        
        i += steps

    return numbers

numbers = make_number(8, 2)

print("The number:")
for num in numbers:
    print(num)
