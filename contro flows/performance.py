def rate_student_performance(score):
 if score >= 80:
    return "Distinction"
 elif 60 <= score <= 70:
    return "Credit"
 elif 40 <= score <= 50:
    return "Fair"
 else:
    return "Fail"
try:
     score = float(input("Enter the students score:"))
     if 0 <= score <= 100:
         rating = rate_student_performance(score)
         print(f"Student's performance: {rating}")
     else:
         print("Invalid score. Please entera score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numerical score.")
     

