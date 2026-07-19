class Quiz:
    # Constructor
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0

        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
                "answer": "B"
            },
            {
                "question": "How many days are there in a week?",
                "options": ["A. Five", "B. Six", "C. Seven", "D. Eight"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
                "answer": "C"
            },
            {
                "question": "What is 5 × 6?",
                "options": ["A. 25", "B. 30", "C. 35", "D. 40"],
                "answer": "B"
            },
            {
                "question": "Which animal is known as the King of the Jungle?",
                "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Bear"],
                "answer": "C"
            }
        ]

    # Function to start the quiz
    def start_quiz(self):
        print("\nWelcome to the Python Quiz,", self.player_name)
        print("Enter A, B, C, or D for each question.\n")

        for question_number, item in enumerate(self.questions, start=1):
            print("Question", question_number)
            print(item["question"])

            for option in item["options"]:
                print(option)

            user_answer = input("Enter your answer: ").upper()

            while user_answer not in ["A", "B", "C", "D"]:
                print("Invalid choice. Please enter A, B, C, or D.")
                user_answer = input("Enter your answer: ").upper()

            if user_answer == item["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect!")
                print("Correct answer:", item["answer"], "\n")

    # Function to display the final result
    def show_result(self):
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100

        print("******** QUIZ RESULT ********")
        print("Player:", self.player_name)
        print("Final Score:", self.score, "out of", total_questions)
        print("Percentage:", percentage, "%")

        if percentage == 100:
            print("Excellent! You got every answer correct.")
        elif percentage >= 60:
            print("Good job! You passed the quiz.")
        else:
            print("Keep practising and try again.")


# Main program
name = input("Enter your name: ")

quiz = Quiz(name)
quiz.start_quiz()
quiz.show_result()