from datetime import datetime

def read():
    global prime_list, prime_dict
    with open('prime_numbers_list_aux.txt', 'r') as f:
        prime_list = [int(i) for i in f]
        prime_dict = {i: prime_list[i] for i in range(0,len(prime_list))}

def get_index(n: int)->int :
    global i
    i = prime_list.index(n)
    return i

def get_prime(i:int)->int :
    prime = prime_list[i]
    return prime


def divisors(n:int):
    global divisors_list, reflected
    divisors_list = []
    for divisor in range(2,n):
        if n % divisor == 0:
            divisors_list.append(str(divisor))
    if divisors_list != []:
        concatened_divisors = ''.join(divisors_list)[::-1]
        reflected = int(concatened_divisors)
        return reflected


def multiplicative(n: int, prime:int)-> bool:
    for element in prime_list:
        print(divisors(element))
        print(element)

read()
multiplicative(21,73)
        # print(divisors_list)
        # print(reflected)
        # if reflected == n :
        #     return True
        # # elif reflected != concatened_divisors:
        # #     return False


def run():
    # read()
    # for element in prime_list:
    #     i = get_index(element)
    #     if i <= 3 or i == 0:
    #         pass
    #     if i >= 4:
    #         if multiplicative(i) == True:
    #             print('The number'+ str(element) +'satisfies the multiplicative preposition')
    #     else:
    #         pass
    # if multiplicative(21) == True:
    #     print('asdafsd')
    pass

if __name__ == '__main__':
    run()