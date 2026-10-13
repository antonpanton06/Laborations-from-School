"""Your main task: Create a score storing program

DETAILS: Create a program that stores players
and their scores in a dictionary and generates
a summary for each player.
YOUR PROGRAM MUST:
• Store each player's scores in a dictionary, using the player's name as the
key and a list of scores as the value.
• Display a menu: Register a player, Add a score, Show summaries, Exit.
• Use a while loop to keep the menu running.
• Allow the user to add a score to an existing player or register a new player.
• Use a for loop to display summaries for all players.
• Write a recursive function calculate_total(values, index) that
returns the total of a list of scores.
• Display each player's scores, total, average, and performance category.
• Use if/elif/else to handle menu choices and determine
performance categories.
• Handle players with an empty score list.
• Use f-strings for formatted output.
Average score Category
Below 10 Low
10-15 (inclusive) Moderate
Above 15 High
No scores recorded N/A
"""

scores = {} # => {player: [10, 21, 30]}

def calculate_total(values, index,):

    # Base case
    if len(values) == index:
        return 0
    
    # Get current score
    current_score = values[index]

    # Recursion step
    return current_score + calculate_total(values, index + 1)
    

def register_player():

    new_player = input("Enter player's name: ") # e.g Anton

    if new_player == None or new_player.strip() == "":   # Handle input
        print("Player name cannot be empty.")
        return new_player
    elif new_player in scores:
        print(f"Player '{new_player}' is already registered.") 
    else:
        print(f"Player '{new_player}' registered successfully.")
        scores[new_player] =[]
    
    return new_player


def add_score():
    # 1. Ask for the player's name
    player_name = input("Player name?: ")
    # 2. Check whether the player exists
    if player_name not in scores:
        print("Player does not exist within dictionary")
    else: 
        # 3. Ask for a score
        try:
            score = int(input("Enter score: "))
            
            # 4. Validate the score
            if score == "":
                print("\nAdded score cannot be empty")
            else:
                # 5. Add the score to the player's list
                scores[player_name].append(score)

                # 6. Print a confirmation
                print(f"Score added successfully: {score}")
                print (scores)
        except ValueError:
            print("Invalid input")
    
    
def show_summaries():

    for player_name, score in scores.items():
        # Calculate player's total
        total = calculate_total(score, 0)

        if len(score) <= 0:
            average = 0
        else:
            average = total / len(score)

        if average == 0:
            category = "N/A"

        elif average < 10:
            category = "Low"

        elif average <= 15:
            category = "Moderate"

        else:
            category = "High"

    # The summary:
    print(f"\nPlayer: {player_name}")
    print(f"Scores: {score}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Performance: {category}")
        
    
def main():
    while True:
        print("\nSCOREBOOK")
        print("1. Register a player")
        print("2. Add a score")
        print("3. Show summaries")
        print("4. Exit")
        try:
            choice = int(input("Choice: "))
            # Handle the choice
            if choice == 1:
                register_player()
            elif choice == 2:
                add_score()
            elif choice == 3:
                show_summaries()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Choose a integer between 1 and 4.")
        except ValueError:
            print("Invalid choice. Choose a integer between 1 and 4.")
            continue

if __name__ == "__main__":
    main()