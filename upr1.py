
def prime_numbers():
    # Outputs a list of prime numbers from 2 to 1000.
    numbers = []
    for n in range(2, 1000):
        fl = 1
        for i in numbers:
            if n % i == 0:
                fl = 0
        if fl == 1:
            numbers.append(n)
    print(numbers)
    

prime_numbers()
