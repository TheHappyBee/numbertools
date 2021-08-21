def iseven(number):
     if number % 2 == 0:
          return True
     elif number % 2 != 0:
          return False
def isodd(number):
     if number % 2 == 0:
          return False
     elif number % 2 != 0 :
          return True
def isprime(number):
     if (number <= 1):
        return False
     for i in range(2, number):
        if (number % i == 0):
            return False
 
     return True
def isgreater(number1, number2):
     if number1 > number2:
          return True
     elif number1 < number2:
          return False
def isless(number1, number2):
     if number1 > number2:
          return False
     elif number1 < number2:
          return True
def isnegitive(number):
     if number < 0:
          return True
     elif number >= 0:
          return False
def isfactor(number, factor):
     if number%factor==0:
          return True
     elif number%factor!=0:
          return False
def ismultiple(number, multiple):
     if multiple%number ==0:
          return True
     elif multiple%number != 0:
          return False
def isLCM(number1, number2, multiple):
     if number1 > number2:
          greater = number1
     else:
          greater = number2

     while(True):
          if((greater % number1 == 0) and (greater % number2 == 0)):
             lcm = greater
             break
          greater += 1

     if lcm == multiple:
        return True
     elif lcm != multiple:
        return False
def isGCF(number1, number2, factor):
     if(number2==0):
        gcf = number1
     else:
        return hcfnaive(number2,number1%number2)
     if gcf == factor:
        return True
     elif gcf != factor:
        return False

def isequal(number1, number2):
     if number1 == number2:
          return True
     elif number1 != number2:
          return False

   
      

     
