principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount : "))
    if principle < 0:
        print("Principle amount should be greater than 0.")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate : "))
    if rate < 0:
        print("Interest rate should be greater than 0.")
    else:
        break

while True:
    time = float(input("Enter the time : "))
    if time < 0:
        print("Time should be greater than 0.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print("Total amount after", time, "years is:", total)
