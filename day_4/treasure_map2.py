row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position1 = int(position[0])
position2 = int(position[1])
horizontal = map[position1 - 1]
horizontal[position2 - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

