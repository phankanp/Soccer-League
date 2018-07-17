from csv import DictReader
import os


# Reads CSV file, converts, and returns a list of player dicts
def players_from_file():
    with open("soccer_players.csv") as file:
        csv_reader = DictReader(file)
        players = list(csv_reader)
    return players


# Return list of players with previous experience
def experienced_players(players):
    exp_players = []

    for row in players:
        if row['Soccer Experience'] == 'YES':
            exp_players.append(row)
    return exp_players


# Returns a list of players without previous experience
def inexperienced_players(players):
    inexp_players = []

    for row in players:
        if row['Soccer Experience'] == 'NO':
            inexp_players.append(row)
    return inexp_players


# Gets 3 players from provided list parameter, adds to, and returns a list
def add_players_to_team(players):
    team = []
    count = 0

    while count < 3:
        team.append(players.pop())

        count += 1

    return team


# Creates a file containing teams and players in each team
def write_teams_to_file(team1, team2, team3):
    with open("teams.txt", "w") as file:
        file.write("Sharks\n")
        for player in team1:
            file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
        file.write("\nDragons\n")
        for player in team2:
            file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
        file.write("\nRaptors\n")
        for player in team3:
            file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")


# Generates welcome letter for each player in the league
def generate_welcome_letters(players):
    dirname = 'welcome letters'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    for player in players:
        file_name = "_".join(player["Name"].lower().split(" ")) + ".txt"
        dirPath = os.path.join(dirname, file_name)

        with open(dirPath, 'w') as file:
            file.write(f"Dear {player['Guardian Name(s)']},\n\n")
            file.write(
                f"Your child, {player['Name']}, has been assigned to the following team: {player['Team Name']}\n")
            file.write(f"The teams's first practice will be on {player['Practice Time']}")
            file.write("\n\nThank You,\nThe Soccer League")


def main():
    # Gets list of players from CSV and separates into two groups
    players = players_from_file()
    experienced = experienced_players(players)
    inexperienced = inexperienced_players(players)

    # Equally adds experiences and inexperienced to each team
    sharks = add_players_to_team(experienced) + add_players_to_team(inexperienced)
    dragons = add_players_to_team(experienced) + add_players_to_team(inexperienced)
    raptors = add_players_to_team(experienced) + add_players_to_team(inexperienced)

    write_teams_to_file(sharks, dragons, raptors)

    # Adds dictionary items for team names and practice times
    for player in sharks:
        player["Team Name"] = "Sharks"
        player["Practice Time"] = "August 1, 2018 @ 4:00PM"
    for player in dragons:
        player["Team Name"] = "Dragons"
        player["Practice Time"] = "August 1, 2018 @ 6:00PM"
    for player in raptors:
        player["Team Name"] = "Raptors"
        player["Practice Time"] = "August 1, 2018 @ 8:00PM"

    all_players = sharks + dragons + raptors

    generate_welcome_letters(all_players)


if __name__ == "__main__":
    main()
