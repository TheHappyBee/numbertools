def issorted(list):
     for n in range(len(list)):
          if list[n] > list[n+1]:
               return False

     return True
def isdivisble(number1, number2):
     if number1 % number2 == 0:
          return True
     else:
          return False
