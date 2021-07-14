Height = float(input('Enter Your height in Centimeters: '))
Weight = float(input('Enter Your Weight: '))
Height = Height/100  # convert into meter
BMI = Weight/(Height*Height)
if BMI > 0:
    if BMI <= 16:
        print('You BMI is: ', BMI)
        print('You are Severely UnderWeight')
    elif BMI <= 18.5:
        print('You BMI is: ', BMI)
        print('You are UnderWeight')
    elif BMI <= 25:
        print('You BMI is: ', BMI)
        print('You are Healthy')
    elif BMI <= 30:
        print('You BMI is: ', BMI)
        print('You are OverWeight')
    else:
        print('You BMI is: ', BMI)
        print('You are Severely OverWeight')
else:
    print('Enter Valid Details: ')
