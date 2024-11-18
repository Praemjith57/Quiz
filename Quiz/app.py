from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz data
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Austen", "Tolkien"], "answer": "Shakespeare"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, question in enumerate(quiz_data):
            selected = request.form.get(f"q{i}")
            if selected == question["answer"]:
                score += 1
        return render_template('result.html', score=score, total=len(quiz_data))
    return render_template('quiz.html', quiz_data=quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
