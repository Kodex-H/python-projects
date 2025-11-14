while True:
    print("========WAEC GRADING SYSTEM======= \n -80-100 ---> A \n -70-79---> B \n -60-69---> C \n -50-59---> D \n -40-49---> E \n -40---> F ")
    choice = input('would you like to continue? (y/n): ').lower()
    if choice == 'n':
        print('thank you for your time ')
        break
    elif choice != 'y' and choice != 'n':
        print('Invalid input')
        continue
    score = int(input("Enter your score: "))
    if score >= 80 and score <= 100:
        print(f"Your score is: {score} you had a A")
        continue
    elif score >= 70 and score <= 79:
        print(f"Your score is: {score} You had a B")
        continue
    elif score >= 60 and score < 70:
        print(f"Your score is: {score} You had a C")
        continue
    elif score >= 50 and score < 60:
        print(f"Your score is: {score} you had a D ")
        continue
    elif score >= 40 and score < 50 :
        print(f"Your score is: {score} you had an E")
        continue
    else:
        print(f"Your score is: {score} you had an F")


