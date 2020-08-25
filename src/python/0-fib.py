import time
import functools

def memo(f):
    m = {}

    @functools.wraps(f)
    def f1(*args):
        k = str(args)
        if k in m:
            return m[k]
        m[k] = f(*args)
        return m[k]

    return f1


@memo
def fib_recursive(n: int) -> int:
    """Determine Fibonacci number recursively.
    Fibonacci is defined as: f(n) = f(n-1) + f(n-2)
    
    Runtime: O(n)       # one call per i in range 0 < i < n
    Memory:  O(n)       # of stored results of the form: n -> f(n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_iterative(n: int) -> int:
    """Determine Fibonacci number iteratively.
    Fibonacci is defined as: f(n) = f(n-1) + f(n-2)
    
    Runtime: O(n)       # one call per i in range 0 < i < n
    Memory:  O(1)       # of stored results of the form: n -> f(n)
    """
    second = 0
    first  = 1
    for _ in range(2, n + 1):
        current = first + second
        second = first
        first = current
    return first


if __name__ == '__main__':
    print('(Press CTRL-C to exit)')
    while True:
        try:
            n = int(input('Enter n for fib(n): '))
        except KeyboardInterrupt:
            print('Exitting.')
            break
        except ValueError as e:
            print(e)
        else:
            start = time.time()
            res   = fib_recursive(n)
            end   = time.time()
            print(f'fib_recursive({n}) = {res}. Took {end - start} seconds.')
            start = time.time()
            res   = fib_iterative(n)
            end   = time.time()
            print(f'fib_iterative({n}) = {res}. Took {end - start} seconds.')


