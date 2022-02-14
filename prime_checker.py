import sys
from datetime import datetime


def prime_checker(number: int) -> int:
    k = 0
    for i in range(1,number+1):
        if number == i or i == 1:
            continue
        if number % i ==0:
            k += 1
    if k == 0:
        return number
    else:
        pass
            
def writting_function(number: int):
    original_stdout = sys.stdout  
    with open('prime_numbers_list.txt', 'a') as f:
            f.write(str(number))
            f.write('\n')


def run_numbers(max_number:int):
    for n in range(1, max_number+1):
        prime_checker(n)
        if prime_checker(n) == n:
            writting_function(n) 

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
    run_numbers(1000000)

if __name__ == '__main__':
    run()