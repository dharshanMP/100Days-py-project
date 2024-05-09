class Q_Brain:
    
    def __init__(self, q_list):

        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def next_question(self):
        c_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number} : {c_question.text} (True/False) : ").lower()
        self.checking_answer(user_input, c_question.answer)

    def still_questions(self):
       if len(self.question_list) > self.question_number:
           return True 
       else:
           False

    def checking_answer(self, user_input, correct_ans):
        if user_input == correct_ans.lower():
            print("It's right answer!...")
            self.score += 1

        else :
            print("Oops it's wrong answer...")
            

        print(f"the correct answer is {correct_ans}.")  
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")

        