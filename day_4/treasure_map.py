row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position1 = int(position[0])
position2 = int(position[1])
if position1 == 1:
    if position2 == 1:
        row1[0] = "X"
    elif position2 == 2:
        row1[1] = "X"
    else:
        row1[2] = "X"
elif position1 == 2:
    if position2 == 1:
        row2[0] = "X"
    elif position2 == 2:
        row2[1] = "X"
    else:
        row2[2] = "X"
else:
    if position2 == 1:
        row3[0] = "X"
    elif position2 == 2:
        row3[1] = "X"
    else:
        row3[2] = "X"
print(f"{row1}\n{row2}\n{row3}")