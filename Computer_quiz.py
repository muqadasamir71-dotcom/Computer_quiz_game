# Write your code
print("=" * 40)
print("        PYTHON QUIZ GAME")
print("=" * 40)

score = 0

# Question 1
print("\n1. What does CPU stand for?")
print("A. Central Processing Unit")
print("B. Computer Personal Unit")
print("C. Central Program Unit")
answer = input("Enter your answer (A/B/C): ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is A.")

# Question 2
print("\n2. Which language are we using?")
print("A. Java")
print("B. Python")
print("C. C++")
answer = input("Enter your answer (A/B/C): ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B.")

# Question 3
print("\n3. Which symbol is used for comments in Python?")
print("A. //")
print("B. <!-- -->")
print("C. #")
answer = input("Enter your answer (A/B/C): ").upper()

if answer == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is C.")

# Question 4
print("\n4. Which function is used to display output in Python?")
print("A. print()")
print("B. input()")
print("C. display()")
answer = input("Enter your answer (A/B/C): ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is A.")

# Question 5
print("\n5. Which data type stores text?")
print("A. int")
print("B. str")
print("C. float")
answer = input("Enter your answer (A/B/C): ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B.")

print("\n" + "=" * 40)
print("           QUIZ RESULT")
print("=" * 40)

print(f"Your Score: {score}/5")

if score == 5:
    print("Excellent! Perfect Score!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")

print("=" * 40)
print("     Thanks for Playing!")
print("=" * 40)
