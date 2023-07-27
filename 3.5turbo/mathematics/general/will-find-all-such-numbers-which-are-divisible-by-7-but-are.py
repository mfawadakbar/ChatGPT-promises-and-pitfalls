def find_numbers():
    numbers = []
    for num in range(1, 101):
        if num % 7 == 0 and num % 5 != 0:
            numbers.append(num)
    return numbers

if __name__ == "__main__":
    result = find_numbers()
    print(result)
