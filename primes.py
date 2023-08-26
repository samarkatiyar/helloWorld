def primes_calculator(start,end):
    if start>end:
        print("---------------Error 2655opt?juhbbbbhb?????/hgcbbvcvbhcxbn---------------")
    else:
        answer_list = []
        primelist = [2,3,5,7,11,13,17,19]
    
        for num in range(start,end):
            i=0
            for prime in primelist:
                if num%prime!=0 or num==prime:
                    i=i+1
                
                else:
                    pass
        
            if i == 8:
                answer_list.append(num)

        print(answer_list)

primes_calculator(2,10)
    