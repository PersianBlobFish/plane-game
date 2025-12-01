name = input("Student name: ")
math = float(input("Math grade: "))
science = float(input("Science grade: "))
english = float(input("English grade: "))

def calculate_average(*grades):
    return sum(grades) / len(grades)
average = calculate_average(math, science, english)
def get_grade(avg):
    match avg:
        case _ if avg >= 90:
            return "A"
        case _ if avg >= 80:
            return "B"
        case _ if avg >= 70:
            return "C"
        case _ if avg >= 60:
            return "D"
        case _:
            return "F"
        
if average < 50:
    status = "Fail"
else:
    status = "Pass"

print(f"Report Card for {name}")
print(f"Average Grade: {average:.2f}")
print(f"Grade: {get_grade(average)}")
print(f"Status: {status}")
