from flask import Flask, request, jsonify
from rag_pipeline import answer_question

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.json
    question = data.get('question')
    answer = answer_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

