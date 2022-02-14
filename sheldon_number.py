from ast import Return
from datetime import datetime

def read():
    global prime_list, prime_dict
    with open('prime_numbers_list.txt', 'r') as f:
        prime_list = [int(i) for i in f]
        prime_dict = {i: prime_list[i] for i in range(0,len(prime_list))}

def get_index(n: int)->int :
    return prime_list.index(n)


def get_prime(i:int)->int :
    prime = prime_list[i]
    return prime

def search(list, prime: int):
    for i in range(len(list)):
        if list[i] == prime:
            return True
    return False

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


def flipping(n: int):
    digits_list = []
    aux_list = []
    for digit in str(n):
        digits_list.append(str(digit))
    if digits_list == aux_list:
        pass
    else:
        return int(''.join(digits_list)[::-1])

def mirror(prime1:int) -> bool:
    in1 = get_index(prime1)
    reflected_prime=flipping(prime1)
    indr = get_index(reflected_prime)
    if search(prime_list, reflected_prime) == True:
        if indr == flipping(in1):
            return True
    else:
        return False

def multiplicative(n: int, prime:int)-> bool:
    if prime == divisors(n):
        return True
    else:
        return False
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron '+ str(time_elapsed.total_seconds())+ ' segundos.')
    return wrapper
    
@execution_time
def run():
    read()
    for prime in prime_list:
        i = get_index(prime)
        if multiplicative(i, prime) == True:
            if mirror(prime) == True:
                print('The number '+str(prime)+' satisfies the mirror and multiplicative preposition')
                print('Therefore '+str(prime)+' is a Sheldon prime') 
        elif multiplicative(i,print) == False:
            continue    # print('The number 'str(prime)+' is not a sheldon number')

if __name__ == '__main__':
    run()