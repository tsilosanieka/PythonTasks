#Input Data
students = [
    ("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85),
    ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)
]

print(f"Original Data: {students}\n")

#Unique Grades
all_scores = [score for name, score in students]

#Convert the list of all scores into a set to automatically remove duplicates
unique_grades = set(all_scores)

print("Unique Grades")
print(unique_grades)


#Top Performers
#key=lambda s: s[1] tells sorted() to use the score (the 2nd element)
#reverse=True sorts from highest to lowest
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

#Get the names (item[0]) from the top 3 sorted tuples using a slice [:3]
top_performers = [name for name, score in sorted_students[:3]]

print("\nTop 3 Performers")
print(top_performers)


#Failed Students
#It keeps the (name, score) tuple only if 'score < 51'
failed_students = [(name, score) for name, score in students if score < 51]

print("\nFailed Students (Score < 51)")
print(failed_students)