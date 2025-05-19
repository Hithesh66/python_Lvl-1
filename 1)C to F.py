#temp in fahrenheit to celsius

f = float(input("enter T in c:"))

c = ((f-32)/1.8)

print(f"{f}in  fahrenheit is equal to {c:.2f}celsius")
#f"..." is directs straight to a string 
#{...} grabs the variable f
#{c:.2f} grabs c value and rounds to 2 decimal places
