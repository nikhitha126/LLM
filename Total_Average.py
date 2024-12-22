def calculate(total,average):
    if average < 70:
        return "Fail", "F"
    elif 70 <= average < 80:
        return "Pass", "C"
    elif 80 <= average < 90:
        return "Pass", "B"
    elif 90 <= average <= 100:
        return "Pass", "A"
    else:
        return "Invalid", "N/A"
number=input("Enter student number: ")
name=input("Enter student name: ")
marks_c=float(input("Enter marks in c: "))
marks_cp=float(input("Enter marks in c++: "))
marks_java=float(input("Enter marks in java: "))
total=marks_c+marks_cp+marks_java
average= total/3
result,grade=calculate(total,average)
print("\n--- Student Report ---")
print(f"Student Number: {number}")
print(f"Student Name: {name}")
print(f"Total Marks: {total:.2f}")
print(f"Average Marks: {average:.2f}")
print(f"Result: {result}")
print(f"Grade: {grade}")