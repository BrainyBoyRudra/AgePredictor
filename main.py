
age = int(input('Hello This Is Standard Predictor Please enter your age to predict your standard(in years). '))
if (age>=2 and age<=5) :
    print('You are in Pre primary')
elif (age >= 6 and age<=10) :
    print('You are in Primary')
elif (age>=0 and age<2):
    print('You are a Infant')
elif (age >=11 and age<=15) :
    print('You are in Secondary')
elif (age>=16 and age<=23) :
    print('you are in college')
elif (age>=24 and age<60):
    print('You are a Graduated Adult')
elif (age>=60):
    print('You are a OldAge Person now')
else :
    print('please enter valid number')