import prime_func_call

n = int(input("Input number : "))

if prime_func_call.prime(n) == False:

    print('{} is not Prime number'.format(n))

else:

    print('{} is Prime number'.format(n))
