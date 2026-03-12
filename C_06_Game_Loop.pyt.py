comp_score = 0
user_score = 0


game_goal = int(input("Game Goal"))
while comp_score < game_goal and user_score < game_goal:
    come_points = int(input("Enter the computer points at the end of the round:"))
    user_points = int(input("Enter the user points at the end of the round"))


    comp_score += come_points
    user_score += user_points

    print("*** Game Update ***")
    print(f"User Score: {user_points} | Computer Score {comp_score}")

print()
if user_score > comp_score:
    print("the user won")
else:
    print("the computer won")
    


