def badge_maker(name):
    print_message = "Hello, my name is " + name + "."
    return print_message

def batch_badge_creator(names):
    list_of_badges = []
    for name in names:
        
        badge = badge_maker(name)
        list_of_badges.append(badge)
    return list_of_badges

def assign_rooms(names):
    new_list = []
    rooms = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for i in range(len(names)):
        print(badge_maker(names[i]))
        welcome_message_room_assignment = "Hello, " + names[i] + "! You'll be assigned to room " + rooms[i] + "!"   
        new_list.append(welcome_message_room_assignment)
       
    return new_list
    

def printer(names):

    batch_badge_creator(names)
    for room_assignment in assign_rooms(names):
        print(room_assignment)


printer(["Arel", "Carol"])