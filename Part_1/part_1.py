# 1. First largest number · Given [12, 5, 8, 20, 15], find the first largest number .

numbers = [12, 5, 8, 20, 15]
largest = max(numbers)
print(largest)

# OR

def find_largest_number(number_list):
    max = number_list[0]
    for i in range(len(number_list)):
        if number_list[i]>max:
            max = number_list[i]
    return max

print(find_largest_number(numbers))




# 2. Character frequency . Given the string 'programming', count the frequency of every character using a dictionary.

def count_characters(st):
    freq = {}
    for ch in st:
        freq[ch] = freq.get(ch,0) + 1
    return freq

print(count_characters('programming'))


# 3. Student marks analysis · Store three students and their marks in a dictionary. Print each student's result as Pass (marks >= 40) or Fail.

student_marks ={

    "John" : 35,
    "Mark" : 55,
    "Albert" : 40
}

for key,value in student_marks.items():
    if value >= 40:
        print(f"{key} passed with {value} marks")
    else:
        print(f"{key} failed with {value} marks")

