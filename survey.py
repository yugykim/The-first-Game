print("Hi. This is a survey regarding to your job satisfaction")
first_q = input("Is job satisfaction important to you? answer yes or No : ").lower()
answer_col = []
if first_q == "yes":
    second_q = input("What is the most important factor to prived your job satisfaction ?")
    answer_col.append(second_q)
    third_q = input('What advice do you have for someone who does not find his/her job satisfying ?')
    answer_col.append(third_q)
else:
    pass

print("Your answer that your job satisfaction is important. Because " + answer_col[0] + '\n and you want to give an advice ' + answer_col[1])
print("Thank you for answering all of the questions")

with open('answers.txt', 'w') as file:
    for answer in answer_col:
        file.write(answer +'\n')

    file.close()
