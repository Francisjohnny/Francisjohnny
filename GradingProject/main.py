student_scores = {
    'Pere': 98, 'Morgan': 46, 'Chin': 87, 'Favor': 76, 'Sara': 53, 'Lemca': 42, 'Tim': 50,
}

print(student_scores["Pere"])
student_scores["Pere"] = 98

#student_grade = {
#   "Scores 86 - 100: Grade = Outstanding.",
#   "Scores_71 - 85: Grade = Exceeds_Expectations.",
#   "Scores 50 - 70: Grade = Acceptable.",
#   "Scores 49 or lower: Grade = Fail.",
#}

# Loop through a dictionary

# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary
for student in student_scores:

    # Get the value (student score) by using the key each time.
    score = student_scores[student]

    # Check what grade the score would get, then add it to student_grades
    if score >= 86:
        student_grades[student] = 'Outstanding'
    elif score >= 71:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 50:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
for key in student_scores:
    score = student_scores[key]
    grade = student_grades[key]
    print(f"name: {key}, Score: {score}, Grade: {grade}")
