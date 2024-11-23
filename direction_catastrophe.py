# Direction Catastrophe
# A very simple problem with many different solutions, but the main aim is to solve it in the most efficient way.
# A man was given directions to go from point A to point B. 
# The directions were: “SOUTH”, “NORTH”, “WEST”, “EAST”. Clearly “NORTH” and “SOUTH” are opposite, “WEST” and “EAST” too. 
# Going to one direction and coming back in the opposite direction is a waste of time and energy. 
# So, we need to help the man by writing a program that will eliminate the useless steps and will contain only the necessary directions. 
# For example: The directions [“NORTH”, “SOUTH”, “SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”] should be reduced to [“WEST”]. 
# This is because going “NORTH” and then immediately “SOUTH” means coming back to the same place. 
# So we cancel them and we have [“SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”]. 
# Next, we go “SOUTH”, take “EAST” and then immediately take “WEST”, which again means coming back to the same point. 
# Hence we cancel “EAST” and “WEST” to giving us [“SOUTH”, “NORTH”, “WEST”]. 
# It’s clear that “SOUTH” and “NORTH” are opposites hence canceled and finally we are left with [“WEST”].

n = int(input('Enter the no. of Steps in direction: '))

dir = [input('Enter the Direction :') for i in range(n)]

i = 0
while i < len(dir):  # Use a while loop to handle index changes
    j = i + 1
    pair_found = False
    while j < len(dir):
        # Check for canceling pairs
        if (dir[i] == 'N' and dir[j] == 'S') or \
           (dir[i] == 'S' and dir[j] == 'N') or \
           (dir[i] == 'E' and dir[j] == 'W') or \
           (dir[i] == 'W' and dir[j] == 'E'):
            # Remove the pair
            dir.pop(j)  # Remove j first as it comes after i
            dir.pop(i)  # Remove i
            pair_found = True
            break  # Restart the loop as indices have changed
        j += 1
    if not pair_found:  # Only move to the next element if no pair was found
        i += 1

print(dir)
