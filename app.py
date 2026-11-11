from flask import Flask, render_template, request, jsonify
from assistant_chatbot import get_chat_response

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/chat", methods=["GET", "POST"])
def chatpage():
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = get_chat_response(question)
        return jsonify({"answer": answer})
    return render_template("chatpage.html")

if __name__ == '__main__':
    app.run(debug=True)