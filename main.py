
print("Moje základní kalkulačka")
print("------------------------")

result = 0

one_number = int(input("Zadej první číslo:\n"))
operation = input("Zadej operaci: +|-|*|/\n")
two_number = int(input("Zadej druhé číslo:\n"))

if operation == "+":
   result = one_number + two_number
elif operation == "-":
    result = one_number - two_number 
elif operation == "*":
    result = one_number * two_number 
else:
    result = one_number / two_number    
    
print(f"{one_number} {operation} {two_number} = {result}")    
   
