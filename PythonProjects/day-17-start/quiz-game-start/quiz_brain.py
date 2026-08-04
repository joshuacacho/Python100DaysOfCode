# TODO 1 - ask the questions
# TODO 2 - checking if the answer was correct
# TODO 3 - checking if we're the enf of the quiz


# Challenge 1
    # Create Class with constructor of question_number set to 0 and question_list
class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Challenge 2
        # create a method next question which
            # retrieves the item at the current question_number from the question_list
                # (in lists index starts at 0 for question 1)
                # (this is why our question_number = 0 starts at 0)
            # Use the input() function to show the user the Question text and ask for the users answer
    def next_question(self):
        current_question = self.question_list[self.question_number] # can pull 'answer' from the question
        self.question_number = self.question_number + 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer) # CALL THE SELF CHECK METHOD BELOW



    # Challenge 3 - continue asking more questions
        # create a method which determines if we have questions or not
            # load next_question -- above
            # user types answer
            # if we still have questions - call this method to determine
                # if true ask a question again
                # if false end game
            # Return boolean if you have more questions or not
    def still_has_questions(self):

        if self.question_number < len(self.question_list):
            more_questions = True
        else:
            more_questions = False

        return more_questions


    # Challenge 4
        # check if the answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1 # increment score
        else:
            print("That is wrong")

        #show correct answer if user got it right or wrong
        print(f"The correct answer was {correct_answer}. ")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n") # leave space for next question







