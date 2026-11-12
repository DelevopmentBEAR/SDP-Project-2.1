# Imports the Flask class and related functions to create a web application
from flask import Flask, render_template, request, jsonify
# Imports the get_chat_response function from the assistant_chatbot module to handle chat responses
from assistant_chatbot import get_chat_response

# Creates an instance of the Flask class to initialize the web application
app = Flask(__name__)

# Defines a route for the homepage of the web application, which renders the homepage.html template
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Defines a route for the chat page of the web application, which handles both GET and POST requests
@app.route("/chat", methods=["GET", "POST"])
def chatpage():
    # If the request method is POST, it retrieves the user's question from the form data, 
    # gets the chat response using the get_chat_response function, and returns the answer as a JSON response
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = get_chat_response(question)
        return jsonify({"answer": answer})
    return render_template("chatpage.html")

# Runs the Flask web application in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)