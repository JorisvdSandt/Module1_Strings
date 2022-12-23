# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#declaring the initial player names (str)
player_goal_0 = "Ruud Gullit"
player_goal_1 = "Marco van Basten"

#declaring the times when the goals are scored (int)
goal_0 = 32
goal_1 = 54

#creating a string with the above variables
scorers = player_goal_0 +  " "  + str(goal_0) + ", " + player_goal_1 +  " " + str(goal_1)

#creating a longer string with the above variables, using 'f strings
report = f'{player_goal_0} scored in the {goal_0}nd minute\n{player_goal_1} scored in the {goal_1}th minute'

# part 2 - declaring a new player name and performing some slicing on it (& finding)
player = 'Erwin Koeman'
find_space = player.find(' ')
first_name = player[:find_space]

last_name = player[find_space+1:]
last_name_len = len(last_name)

name_short = player[0] + ". " + last_name

chant =  (first_name + "! ") * len(first_name)
chant = chant[:-1]

good_chant = chant[-1] != " "
