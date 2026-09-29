scores = []

def process_scores(values, index):
    score = 0
    
    # Check whether the end of the list has been reached
    if index == len(values):
        return 0

    # Get the current score
    score = values[index]

    # Handle negative scores
    if score < 0:
        score = abs(score) * 2

    # Recursively process the next score
    return score + process_scores(values, index + 1)


def main():
    
    print("PENALTY SCORE CALCULATOR\nEnter scores one at a time.\nEnter q to finish.")

    score = input("Score: ")

    while score != "q":

    # Add the score to the list
        scores.append(int(score))
        score = input("Score: ")
    print("\nEnd of the list is reached!")

    # Calculate the total
    total = process_scores(scores, 0)

    # Print the result
    print(f"Scores: {scores}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()