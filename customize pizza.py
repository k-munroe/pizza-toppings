print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_cost = 0

if size == "S":
    total_cost += 15
    if add_pepperoni == "Y":
        total_cost += 2
        if extra_cheese == "Y":
            total_cost += 1
        else:
            total_cost += 0
        
        
    elif add_pepperoni =="N":
        total_cost += 0
        if extra_cheese == "Y":
            total_cost += 1
        else:
            total_cost += 0
        
    
elif size == "M":
    total_cost += 20
    if add_pepperoni == "Y":
        total_cost += 3
        if extra_cheese == "Y":
            total_cost += 1
        else:
            total_cost += 0
        
    elif add_pepperoni == "N":
        total_cost += 0
        if extra_cheese == "Y":
            total_cost += 1
        else:
            total_cost += 0
        
elif size == "L":
    total_cost += 25
    if add_pepperoni == "Y":
        total_cost += 3
        if extra_cheese == "Y":
            total_cost += 1
        else:
            total_cost += 0
        
    elif add_pepperoni =="N":
        total_cost += 0
        if extra_cheese == "Y":
            total_cost += 1
        else:
            total_cost += 0
        
    
else:
    print("Enter correct response.")
print(f"Your total cost is {total_cost}.")