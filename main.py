from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for i in question_data:
    qu = Question(i['text'], i['answer'])
    question_bank.append(qu)

quiz = QuizBrain(question_bank)

is_on = True

while is_on:
  quiz.answer_checking()
  is_on = quiz.questions_checking()
  print("\n")
  
print(f"Your final score {quiz.score}/{quiz.question_number} 😎")

# check out more questions in "https://opentdb.com/"