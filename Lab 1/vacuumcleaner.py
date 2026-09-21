rooms = {'A': 'Dirty','B': 'Clean'}
vacuum_location = 'B'
print("Start State -> Rooms: ",rooms," \nVacuum is in: ",vacuum_location)
while True:
    current_status = rooms[vacuum_location]
    if current_status == 'Dirty':
        print("Room",vacuum_location,"is Dirty. Cleaning...")
        rooms[vacuum_location] = 'Clean' 
    else:
        print("Room ",vacuum_location," is Clean.")
        if vacuum_location == 'A':
            vacuum_location = 'B'
        else:
            vacuum_location = 'A'
        print("Moving to Room ",vacuum_location)
    print("Current Room Status: ",rooms)
    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("All rooms are clean.")
        break
