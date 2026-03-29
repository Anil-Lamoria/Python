# Simple interest calculator

Principal = float(input("Enter principal: "))
Rate_of_interest = float(input("Enter Rate of Interest: "))
Time = float(input("Enter Time(in year): "))

Simple_interest = (Principal * Rate_of_interest * Time)/100
print("Simple interest", Simple_interest)