import requests
import html
import random
import time

def fetch_trivia_questions(amount=10, category=None, difficulty=None):
    """
    Fetch trivia questions from Open Trivia Database API
    """
    url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple"}
    
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []

def display_question(question_data, question_num, total):
    """
    Display a trivia question with multiple choice answers
    """
    print(f"\n{'='*60}")
    print(f"Question {question_num}/{total}")
    print(f"Category: {html.unescape(question_data['category'])}")
    print(f"Difficulty: {question_data['difficulty'].capitalize()}")
    print(f"{'='*60}")
    print(f"\n{html.unescape(question_data['question'])}\n")
    
    # Combine correct and incorrect answers
    answers = question_data["incorrect_answers"] + [question_data["correct_answer"]]
    random.shuffle(answers)
    
    # Display options
    for idx, answer in enumerate(answers, 1):
        print(f"{idx}. {html.unescape(answer)}")
    
    return answers

def get_user_answer(num_options):
    """
    Get and validate user's answer
    """
    while True:
        try:
            answer = input(f"\nYour answer (1-{num_options}): ").strip()
            answer_num = int(answer)
            if 1 <= answer_num <= num_options:
                return answer_num
            print(f"Please enter a number between 1 and {num_options}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nQuiz interrupted by user.")
            exit(0)

def play_trivia():
    """
    Main function to run the trivia game
    """
    print("\n" + "="*60)
    print("Welcome to Random Trivia CLI!".center(60))
    print("="*60)
    
    # Get number of questions
    while True:
        try:
            num_questions = input("\nHow many questions? (1-50, default 10): ").strip()
            num_questions = int(num_questions) if num_questions else 10
            if 1 <= num_questions <= 50:
                break
            print("Please enter a number between 1 and 50")
        except ValueError:
            print("Invalid input, using default (10)")
            num_questions = 10
            break
    
    print("\nFetching questions...")
    questions = fetch_trivia_questions(amount=num_questions)
    
    if not questions:
        print("Failed to fetch questions. Please try again later.")
        return
    
    score = 0
    total = len(questions)
    
    for idx, question in enumerate(questions, 1):
        answers = display_question(question, idx, total)
        user_answer_idx = get_user_answer(len(answers))
        
        correct_answer = html.unescape(question["correct_answer"])
        user_answer = html.unescape(answers[user_answer_idx - 1])
        
        if user_answer == correct_answer:
            print("\n✓ Correct!")
            score += 1
        else:
            print(f"\n✗ Wrong! The correct answer was: {correct_answer}")
        
        time.sleep(1)
    
    # Display final score
    print("\n" + "="*60)
    print(f"Quiz Complete! Your score: {score}/{total} ({(score/total)*100:.1f}%)".center(60))
    print("="*60)

if __name__ == "__main__":
    play_trivia()
