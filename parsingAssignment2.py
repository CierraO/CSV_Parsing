############################## PART A ##############################
def find_matches(team):
    match_schedule = open("Scouting_2019_Match_Schedule.csv", "r")
    
    print(team + ": ", end = '')

    for line in match_schedule.readlines():
        # Turn each line into a list of all the numbers
        line = line.split("\n")
        line = line[0]
        line = line.split(",")
        
        # If a number in the second through the seventh row = the team number,
        # the team is in that match
        for i in range(1,7):
            if line[i] == team:
                print(line[0] + ", ", end = '')
                break
    print("\n")

    match_schedule.close()


find_matches("2168")


############################## PART B ##############################
match_schedule = open("Scouting_2019_Match_Schedule.csv", "r")

counter = 0
all_teams = []
team_repeated = 0

# Get a list of all teams
for line in match_schedule.readlines():
    if counter > 0:
        # Turn each line into a list of all the numbers
        line = line.split("\n")
        line = line[0]
        line = line.split(",")

        # Go through every team in the row
        for i in range (1,7):
            # Check if the team has already been added to the list
            for team in all_teams:
                if team == line[i]:
                    team_repeated += 1
                    break
            # If the team wasn't added to the list yet, add it
            if team_repeated == 0:
                all_teams.append(line[i])
    counter += 1
match_schedule.close()

# Print matches of all teams
for team in all_teams:
    find_matches(team)
