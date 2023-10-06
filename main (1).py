def CheckLeap(Year):  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("the given Year is a leap Year");   
  else:  
    print ("the  given Year  is not a leap Year") 
Year = int(input("Enter the year: "))  
CheckLeap(Year)  

