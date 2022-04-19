class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question} (True/False)? ")

    def answer_checking(self):
        answer = self.question_list[self.question_number].answer
        the_answer = QuizBrain.next_question(self)
      
        if the_answer.lower() == answer.lower():
            self.score += 1 
            print(f"You got it right👾👾👾!!! \nThe correct answer was: {answer}. \nYour current score is: {self.score}/{self.question_number}")

        else:
            print(f"Sorry wrong answer😫 \nThe correct answer was: {answer}. \nYour current score is: {self.score}/{self.question_number}")

    def questions_checking(self):
        if self.question_number < len(self.question_list):
          return True
        else:
          return False
            
          
            
