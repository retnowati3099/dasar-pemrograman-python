def check_pass(score):
    if score >= 60 and score <= 100:
        print("Lulus")
    else:
        print("Tidak lulus")


score = int(input("Enter your score: "))
check_pass(score)
