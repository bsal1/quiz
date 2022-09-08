questions=["What is the capital of Nepal ?",
            "Who is the first king of Nepal ?",
            "Who developed python ?"]

answers=["kathmandu",
         "prithvi narayan shah",
         "guido van rossum"]
score=0
        
for i in range(0,len(questions)):
    print(questions[i])
    if input("Ans : ").lower()==answers[i]:
        print("Correct \n")
        score+=1
    else :
        print("Wrong\n")
print(f"\nYour score : {score}/3\n")