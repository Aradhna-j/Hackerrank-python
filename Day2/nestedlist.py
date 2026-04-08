'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.'''
if __name__ == '__main__':
    
    students = []

    # Step 1: Take input and store
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Step 2: Extract all scores
    scores = []
    for student in students:
        scores.append(student[1])

    # Step 3: Remove duplicates and sort
    unique_scores = list(set(scores))
    unique_scores.sort()

    # Step 4: Get second lowest score
    second_lowest = unique_scores[1]

    # Step 5: Find names with second lowest score
    names = []
    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    # Step 6: Sort names alphabetically
    names.sort()

    # Step 7: Print names
    for name in names:
        print(name)
