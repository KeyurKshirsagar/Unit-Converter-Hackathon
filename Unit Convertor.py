print("Keyur Kshirsagar \nDelhi Private School Dubai \nkeyurkshirsagar@gmail.com")
print("MENU: \n1-Mass \n2-Length \n3-Speed \n4-Temperature \n5-Currency \n6-Date")
print()
a=int(input("Kindly select the required converter:"))

if a==1:
    print("Welcome to Mass Converter")
    print()
    print("Menu:\n1-Pounds and Kilograms \n2-Stone and Pounds \n3-Stone and Kilograms")
    print()
    b=int(input("Select the required conversion:"))
    
    if b==1:
        d=int(input("Enter the value:"))
        print()
        po=d*2.205
        kg=d/2.205
        print("The value of",d,"Kilograms is",po,"Pounds")
        print("The value of",d,"Pounds is",kg,"Kilograms")

    elif b==2:        
        d=int(input("Enter the value:"))
        print()
        po=d*14
        st=d/14
        print("The value of",d,"Stones is",po,"Pounds")
        print("The value of",d,"Pounds is",st,"Stones")

    elif b==3:
        d=int(input("Enter the value:"))
        print()
        kg=d*6.35
        st=d/6.35
        print("The value of",d,"Stones is",kg,"Kilograms")
        print("The value of",d,"Kilograms is",st,"Stones")
  
    else:
        print()
        print("Select the appropriate value")



elif a==2:
    print("Welcome to Length Converter")
    print()
    print("Menu: \n1-Inches and Centimetres \n2-Yards and Metres \n3-Miles and Kilometre")
    print()
    b=int(input("Select the required conversion:"))
    
    if b==1:
        d=int(input("Enter the value:"))
        print()
        cm=d*2.54
        inch=d/2.54
        print("The value of",d,"Inches is",cm,"Centimeter")
        print("The value of",d,"Centimeter is",inch,"Inches")

    elif b==2:
        d=int(input("Enter the value:"))
        print()
        yr=d*1.094
        m=d/1.094
        print("The value of",d,"Meters is",yr,"Yards")
        print("The value of",d,"Yards is",m,"Meters")

    elif b==3:
        d=int(input("Enter the value:"))
        print()
        km=d*1.609
        mi=d/1.609
        print("The value of",d,"Miles is",km,"Kilometers")
        print("The value of",d,"Kilometers is",mi,"Miles")
        
    else:
        print()
        print("Select the appropriate value")


elif a==3:
    print("Welcome to Speed Converter")
    print()
    print("Menu:\n1-Miles per hour and Kilometres per hour \n2-Knots and miles per hour \n3-Knots and kilometres per hour")
    print()
    b=int(input("Select the required conversion:"))
    if b==1:
        d=int(input("Enter the value:"))
        print()
        mph=d/1.609
        kmph=d*1.609
        print("The value of",d,"Miles per hour is",kmph,"Kilometers per hour")
        print("The value of",d,"Kilometers per hour is",mph,"Miles per hour")

    elif b==2:
        d=int(input("Enter the value:"))
        print()
        mph=d/1.151
        knots=d*1.151
        print("The value of",d,"Miles per hour is",knots,"Knots")
        print("The value of",d,"Knots is",mph,"Miles per hour")

    elif b==3:
        d=int(input("Enter the value:"))
        print()
        knots=d/1.852
        kmph=d*1.852
        print("The value of",d,"Knots is",kmph,"Kilometers per hour")
        print("The value of",d,"Kilometers per hour is",knots,"Knots")

    else:
        print()
        print("Select the appropriate value")

    

elif a==4:
    print("Welcome to Temperature Converter")
    print()
    print("Menu:\n1-Fahrenheit and Celsius \n2-Kelvin and Fahrenheit \n3-Kelvin and Celsius")
    print()
    b=int(input("Select the required conversion:"))
    if b==1:
        d=int(input("Enter the value:"))
        print()
        far=(d*(9/5))+32
        cel=(d-32)*(5/9)
        print("The value of",d,"Celsius is",far,"Farenheit")
        print("The value of",d,"Farenheit is",cel,"Celsius")

    elif b==2:
        d=int(input("Enter the value:"))
        print()
        far=(d-273.15)*(9/5)+32
        kel=(d-32)*(5/9)+273.15
        print("The value of",d,"Kelvin is",far,"Farenheit")
        print("The value of",d,"Farenheit is",kel,"Kelvin")

    elif b==3:
        d=int(input("Enter the value:"))
        print()
        kel=d+273.15
        cel=d-273.15
        print("The value of",d,"Celsius is",kel,"Kelvin")
        print("The value of",d,"Kelvin is",cel,"Celsius")
        
    else:
        print()
        print("Select the appropriate value")
   
    

elif a==5:
    print("Welcome to Currency Converter")
    print()
    print("Menu:\n1-AED and USD  \n2-GBP and USD  \n3-AED and GBP")
    print()
    b=int(input("Select the required conversion:"))
    if b==1:
        d=int(input("Enter the value:"))
        print()
        AED=d*3.6725
        USD=d*0.2722
        print("The value of",d,"AED is",USD,"USD")
        print("The value of",d,"USD is",AED,"AED")

    elif b==2:
        d=int(input("Enter the value:"))
        print()
        GBP=d*0.7893
        USD=d*1.2668
        print("The value of",d,"GBP is",USD,"USD")
        print("The value of",d,"USD is",GBP,"GBP")

    elif b==3:
        d=int(input("Enter the value:"))
        print()
        AED=d*4.6522
        GBP=d*0.2149
        print("The value of",d,"GBP is",AED,"AED")
        print("The value of",d,"AED is",GBP,"GBP")

    else:
        print()
        print("Select the appropriate value")
        
elif a==6:
    print("Welcome to Date Converter")
    print()
    yr=int(input("Enter the YEAR:"))
    mn=int(input("Enter the MONTH:"))
    da=int(input("Enter the DAY:"))
    def gregorian_to_julian(year, month, day):
        i = int((month - 14) / 12)
        jd = day - 32075
        jd += int((1461 * (year + 4800 + i)) / 4)
        jd += int((367 * (month - 2 - (12 * i))) / 12)
        jd -= int((3 * int((year + 4900 + i) / 100)) / 4)
        return jd
    da=gregorian_to_julian(yr, mn,da)
    print("The date in Julian Calendar is",da)
    
else:
    print("Please select a value from the given menu")

while a<=6 and b<=3:
    print()
    print("Thank you for using the unit converter, To use it again please run the program again!!")
    break
