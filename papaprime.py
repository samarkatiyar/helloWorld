def efficient_prime(num):
    for i in range(2,int(num/2)+1):
        if num%i ==0:
            return False
    return True
def primes_in_range(start,end):
    prime_num_list=[]
    for i in range(start,end+1):
        if efficient_prime(i):
           prime_num_list.append(i)
    return prime_num_list

prime_list = primes_in_range(1900000,1901000)
print(prime_list)
print(len(prime_list))
exit(0)    
cum=0
for i in range(1,100):
    prime_list = primes_in_range(1 + cum,1000 + cum)
    print( " Prime numbers between {} and {} --> {}".format(1+cum, 1000+cum, len(prime_list)))
    cum = cum + 1000
