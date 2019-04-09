# 0 books = 0 points
# 2 books = 5 points
# 4 books = 15 points
# 6 books = 30 points
# 8+ books = 60 points

#Code begins here

#Book Club Points
books = int(input('How many books did you purchase this month?'))

if books <= 1:
   print ('0 Points awarded this month')

elif books >=2 and books <= 3:
   print ('5 points awarded this month')

elif books >= 4 and books <= 5:
   print ('15 points awarded this month')

elif books >= 6 and books <= 7:
   print ('30 points awarded this month')

elif books >= 8:
   print ('60 points awarded this month')

else:
   print ('Invalid input!')
   
   
   
#Shipping Charges
lbs = float(input('What is the weight of your package in pounds?'))

if lbs > 0 and lbs <= 2:
   total = lbs * 1.50
   print ('Your total shipping charge is : $', format(total, '.2f')
   
elif lbs > 2 and lbs <= 6:
   total = lbs * 3
   print ('Your total shipping charge is: $', format(total, '.2f')  

elif lbs > 6 and lbs <= 10:
   total = lbs * 4
   print ('Your total shipping charge is: $', format(total, '.2f')   

elif lbs > 10:
   total = lbs * 4.75
   print ('Your total shipping charge is: $', format(total, '.2f')

else:
   print ('Invalid input!')