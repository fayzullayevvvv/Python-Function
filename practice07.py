def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def ask_question(question: str, correct_answer: str):
    user_answer = input(question + ': ')
    if check_answer(user_answer, correct_answer):
        print("To'g'ri")
    else:
        print("Xato")

ask_question('python nima?', 'dasturlash tili')