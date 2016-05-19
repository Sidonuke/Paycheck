rate = input('How much do you make per hour?') #how much do people make?
hours = input('Hours worked?') #Input how many hours worked in 1 hour

if float(hours) > 40: #greater than 40?
    total = 0 #starting point
    x = 0 #starting point
    y = 40 * float(rate) # Base Pay overall.
    x += float(hours) - 40 #Calculate the remainder after the standard 40 hours.
    total += (x * float(rate) * 1.5) # Remainder multiplied by time and a half standard (1.5).
    print ('Overtime worked: ' , float("{0:.2f}".format(x))) #Displayed hours of overtime worked.
    print ('Total Overtime Pay: ' , float("{0:.2f}".format(total)))
    print ('Total Pay with overtime included: ' , float("{0:.2f}".format((y + total))))# Total gross wage.
    print ('Your social security withheld was: ' , float("{0:.2f}".format(((y + total) * .062)))) #Lovely social security tax deduction.
    print ('Your medicare witheld was: ' , float("{0:.2f}".format((y + total) * .0145))) #Lovely medicare deduction.
else:
    z = float(hours) * float(rate)
    print ('Your total pay for this week is: ' , float("{0:.2f}".format(z))) #Total gross wage if less than 40 hours worked.
    print ('Your social security withheld was: ' , float("{0:.2f}".format(z * .062))) #Lovely social security tax deduction.
    print ('Your medicare withheld was: ' , float("{0:.2f}".format(z* .0145)))#Lovely medicare deduction.
