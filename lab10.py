PASSING_SCORE = 50
PASSING_AVERAGE = 60

def study_score_report(scores):
    total = sum(scores)
    passing_count = 0

    for score in scores:
        if score >= PASSING_SCORE:
            passing_count += 1

    if len(scores) == 0:
        average = 0
    else:
        average = total / len(scores)

    if average >= PASSING_AVERAGE:
        result = "Pass"
    else:
        result = "Fail"
        
    return average, passing_count, result

scores = [45, 50, 72, 83]
average, passing_count, result = study_score_report(scores)
print("STUDY SCORE REPORT")
print(f"Scores: {scores}")
print(f"Average: {average:.2f}")
print(f"Passing scores: {passing_count}")
print(f"Result: {result}")

study_score_report(scores)