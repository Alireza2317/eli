#3 cups problem
swaps = input("insert the sequence of swaps: ")

ball_location = 1

for swap_type in swaps:
    if swap_type == "A" and ball_location == 1:
        ball_location = 2
    elif swap_type == "A" and ball_location == 2:
        ball_location = 1
    elif swap_type == "B" and ball_location == 2:
        ball_location = 3
    elif swap_type == "B" and ball_location == 3:
        ball_location = 2
    elif swap_type == "C" and ball_location == 1:
        ball_location = 3
    elif swap_type == "C" and ball_location == 3:
        ball_location = 1
    else:
        print(f"uknown swap type {swap_type}")
print(f"The ball at the end is in {ball_location}")
 