# Question 10: Text file
# Create a file named notes.txt and write five lines into it. Then:
# ●	Read and print the complete file.
# ●	Print only the third line.
# ●	Append one more line without deleting existing content.

filepath = r"C:\Users\314087\Repos\python-playwright\Part_3\notes.txt"
with open(filepath, "w") as file:
    file.write("This is line 1")
    file.write("\nThis is line 2")
    file.write("\nThis is line 3")
    file.write("\nThis is line 4")
    file.write("\nThis is line 5")

with open(filepath, "r") as file:
    content = file.read()
print(content)

with open(filepath, "r") as file:
    file.readline()
    file.readline()
    print("Line 3: ",file.readline())

with open(filepath, "a") as file:
    file.write("\nThis is appended line")

with open(filepath, "r") as file:
    appended_content = file.read()

print(appended_content)



# Question 11: CSV file
# Create employees.csv with the columns id, name, and salary.

import csv

data = [
    ["ID", "Name", "Salary"],
    ["001", "Mark", "50000"],
    ["002", "Anthony", "2000"],
    ["003", "Edward", "70000"],
    ["004", "Ajay", "100000"],
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Csv File Created")