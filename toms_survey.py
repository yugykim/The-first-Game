class survey:
    class surveyQuestion:
        def __init__(self, question, answer=None):
            self.question = question
            self.answer = answer

    def __init__(self, questions):
        self.questions = []
        for q in questions:
            self.questions.append(self.surveyQuestion(q))            
    
    def run(self):
        ex = self.surveyQuestion('this is a survey question')
        print(ex.question)
        print("Hi. This is a survey regarding to your job satisfaction\nIs job satisfaction important to you? answer yes or No :")
        if input().lower() == "yes":
            for q in self.questions:
                print(q.question)
                q.answer = input()

        print("Thank you for answering all of the questions")

    def save(self, filename='answers.txt'):
        with open(filename, 'w') as file:
            for q in self.questions:
                file.write(q.question + ":\n")
                file.write(q.answer + "\n\n")
            file.close()


jobSatisfactionSurvey = survey(["What is the most important factor to prived your job satisfaction ?", "What advice do you have for someone who does not find his/her job satisfying ?"])

jobSatisfactionSurvey.run()
jobSatisfactionSurvey.save()
