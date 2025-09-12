temp = eval(input("Enter your temperature: "))

if temp <= 0:
    print("Temperature is considered below freezing")
elif temp >= 1 and temp <= 15:
    print("Temperature is considered extremely cold")
elif temp >= 16 and temp <= 30:
    print("Temperature is considered cold")
elif temp >= 31 and temp <= 38:
    print("Temperature is considered lukewarm")
elif temp >= 39 and temp <= 42:
    print("Temperature is considered warm")
elif temp >= 43 and temp <= 50:
    print("Temperature is considered Hot")
elif temp >= 51 and temp <= 60:
    print("Temperature is considered extremely hot")
else:
    print("Temeperature is considered burning")