numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15]
primes = list()
not_primes = list()
for i in numbers:
    if i > 1:
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            primes.append(i)
        else:
            not_primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)
