from concurrent.futures import ProcessPoolExecutor
from time import sleep
from validate_prime import is_prime, PRIMES

executor = ProcessPoolExecutor(4)
futures = [executor.submit(is_prime, p) for p in PRIMES[:6]]

while not all(map(lambda f: f.done(), futures)):
    print('do sth else, waiting')
    sleep(1)

print([f.result() for f in futures])
