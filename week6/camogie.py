
#initialize empty list for teams, wins per team, last wins
teams_list = []
wins_list = []
winners = []
last_win_list = []
appearances = []
last_appearance = []
win_percentage_list = []

with open("camogie.csv", "r") as file:
    #read the hgeaders
    headers = file.readline()
    
    #loop through remaining lines of data
    for data_line in file:
        #set variables
        team, wins, last_final_won, runner_up, last_final_lost, total_apperances = data_line.split(",")
        
        #append teams to the teams_list
        teams_list.append(team)
        wins_list.append(int(wins))
        last_appearance.append(last_final_won)
        if last_final_won != "-":
            last_win_list.append(int(last_final_won))
        if int(wins) >0:
            winners.append(team)
        appearances.append(int(total_apperances))


unique_teams_list = sorted(set(teams_list))
unique_wins_list = sorted(set(winners))

#number of counties to aapear in all ireland final
num_of_counties = len(teams_list)
print(f"Number of Counties: {num_of_counties}")

#number of finals
finals = sum(wins_list)
print(f"Total number of All-Ireland finals: {finals}") 

#number of finals
average = sum(wins_list) / len(teams_list)
print(f"Average number of wins per county: {average}")  

#current champs
index = last_win_list.index(2022)
current_champions = unique_wins_list[index]
print(f"Current champions (winners in 2022): {current_champions}") 

#Most Wins
max_most_wins = max(wins_list)
most_wins_index = wins_list.index(max_most_wins)
most_wins = unique_wins_list[most_wins_index]
index_of_last_win = last_win_list[most_wins_index]
print(f"Most wins: {most_wins} with {max_most_wins} wins, most recently in {index_of_last_win}")  

#Highest winning percentage
win_percentage_list =[]
for i, t in zip(wins_list, appearances):
    winning_percent = (i / t)* 100
    win_percentage_list.append(winning_percent)
highest_ratio = max(win_percentage_list)
team_with_highest_ratio_index = win_percentage_list.index(highest_ratio)
team_with_highest_ratio = teams_list[team_with_highest_ratio_index]
most_recent_win = last_appearance[team_with_highest_ratio_index]
print(f"Highest Win Ratio: {team_with_highest_ratio} with {highest_ratio:.0f}%, most recently in {most_recent_win}")  
         
    