from datetime import datetime

def read():
    global prime_list, prime_dict
    with open('prime_numbers_list_aux.txt', 'r') as f:
        prime_list = [int(i) for i in f]
        prime_dict = {i: prime_list[i] for i in range(0,len(prime_list))}

def get_index(n: int)->int :
    return prime_list.index(n)

def get_prime(i:int)->int :
    prime = prime_list[i]
    return prime


def divisors(n:int):
    global divisors_list, reflected
    divisors_list = []
    aux_list = []
    for divisor in range(2,n):
        if n % divisor == 0:
            divisors_list.append(str(divisor))
    if divisors_list == aux_list:
        pass
    else:
        concatened_divisors = ''.join(divisors_list)[::-1]
        reflected = int(concatened_divisors)
        return int(''.join(divisors_list)[::-1])


def multiplicative(n: int, prime:int)-> bool:
    if prime == divisors(n):
        return True
    else:
        return False

def run():
    read()
    for prime in prime_list:
        i = get_index(prime)
        if multiplicative(i, prime) == True:
            print('The number '+ str(prime) +' satisfies the multiplicative preposition')
        elif multiplicative(i,print) == False:
            print('The number '+ str(prime) +' does not satisfies the multiplicative preposition')

if __name__ == '__main__':
    run()