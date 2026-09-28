environment = {"A": "Dirty","B": "Dirty"}
model = {"A": "Unknown","B": "Unknown"}
obstacles = {"A": True,"B": False}
location = "A"
for i in range(4):
    status = environment[location]
    model[location] = status
    print("Location:", location)
    print("Status:", status)
    if status == "Dirty":
        action = "Suck"
    elif location == "A":
        if obstacles["B"]:
            action = "No Op"
        else:
            action = "Move Right"
    elif location == "B":
        if obstacles["A"]:
            action = "No Op"
        else:
            action = "Move Left"
    print("Action:", action)
    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"
    print()
