num=-1
while num <0:
   num=int(input("Enter a number ==>  "))
   if num < 0:
      print (" ERROR! Please provide a number greater than zero :(")

start = 0 
end = num 
mid = (start + end)/2

diff = num - (mid * mid * mid)
i=1
while ( abs(diff) >= 0.00001):
   if diff <0:
      end = mid
   if diff >=0:
      start = mid
   print("{} Start is {} and end is {}".format(i,start,end))
   i=i+1   
   mid = (start + end) / 2
   diff = num - (mid * mid * mid)

print("The cube root is ==> {}".format(round(mid,6)))   