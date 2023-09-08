def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    badges = [(f"Hello, my name is {badge}.") for badge in names]
    return badges

def assign_rooms(names):
    room_assignments = list()
    i= 0
    while i < 8:
        message = f"Hello, {names[i]}! You'll be assigned to room {i + 1}!"
        room_assignments.append(message)
        i += 1
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    assignments = assign_rooms(names)
    for rooms in assignments:
        print(rooms)


