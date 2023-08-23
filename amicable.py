# https://www.codewars.com/kata/56b5ebaa26fd54188b000018

def amicableNumbers(num1, num2):
    sum1=0
    sum2=0
    for i in range(1,num1):
        if num1%i==0:
            sum1+=i
    for j in range(1,num2):
        if num2%j==0:
            sum2+=j
    if(sum1==num2 and sum2==num1):
        return True
    else:
        return False

results = amicableNumbers(220,284)
ressults = amicableNumbers(220,180)
print(results)
print(ressults)