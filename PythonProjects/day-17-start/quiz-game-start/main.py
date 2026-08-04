


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Challenge is to create the question_bank
    # Loop through the data, and pull text and answer out using their keys:
    # in question_data we have created our OWN key:pair values of text:answer so we need to reference those

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Challenge 2
    # to use the new QuizBrain and pass in the question_bank list
quiz_1 = QuizBrain(question_bank) # 12 items in our self.question_list
quiz_length = len(question_bank)
print(quiz_length)


# Challenge 3
    # to continue showing new questions
while quiz_1.still_has_questions():
    quiz_1.next_question()   # already increments so no need to there

# Could also put print statement inside the quiz_brain still_has_questions() method
    # BUT YOU WOULD NOT WANT TO DO IT HERE
        # Why? Because the still_has_questions responsibility is just to check if we have questions left, thats it
print(f"You have completed the quiz")
print(f"Your final score was {quiz_1.score}/{quiz_1.question_number}")







