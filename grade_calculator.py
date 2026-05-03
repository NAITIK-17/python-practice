subjects = ["Maths", "Science", "SST", "English", "Hindi"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = int(input(f"Enter {subject} marks (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("❌ Marks must be 0-100")
        except:
            print("❌ Enter valid number")

total = sum(marks)
percentage = (total / 500) * 100


if percentage >= 95 and percentage <= 100:
    print("Grade: A+")
elif percentage >= 90 and percentage <95:
    print("Grade: A")
elif percentage >= 85 and percentage < 90:
    print("Grade: A-")
elif percentage >= 80 and percentage < 85:
    print("Grade: B+")
elif percentage >= 75 and percentage < 80:
    print("Grade: B")
elif percentage >= 70 and percentage < 75:
    print("Grade: B-")
elif percentage >= 65 and percentage< 70:
    print("Grade: C")
elif percentage >= 60 and percentage < 65:
    print("Grade: D")
elif percentage >= 0 and percentage < 60:
    print("Grade: F")
else:
    print("Enter Your Real Marks!")
