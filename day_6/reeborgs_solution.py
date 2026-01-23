def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    if not at_goal():
        if front_is_clear():
            move()
            if not at_goal():
                if right_is_clear():
                    turn_right()
                    move()
    if not at_goal():
        if not front_is_clear() and not right_is_clear():
            turn_left()