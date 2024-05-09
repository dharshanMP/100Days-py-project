from question_model import Quiz_Question
from data import question_data
from quiz_brain import Q_Brain

question_bank = []

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    question = Quiz_Question(quiz_text = text, quiz_answer = answer)
    question_bank.append(question)

quiz = Q_Brain(q_list = question_bank)  

while quiz.still_questions():
    quiz.next_question()


print("End of quiz")
print(f"your final score is {quiz.score}/{len(question_bank)}")