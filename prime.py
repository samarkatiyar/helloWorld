def primes_calculator(start,end):
    answer_list = []
    primelist = [2,3,5,7,11,13,17,19]
    
    for num in range(start,end):
        i=0
        for prime in primelist:
            if num%prime!=0:
                i=i+1
                
            else:
                pass
        if i == 8:
            answer_list.append(num)

    print(answer_list)

primes_calculator(5000,10000)
