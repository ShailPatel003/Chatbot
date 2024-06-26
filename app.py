from flask import Flask, render_template, request, jsonify
from chat import get_response

# app = Flask(__name__)
app = Flask(__name__,template_folder="templates")

@app.get("/")
def index_get():
    return render_template("base.html")


# test
@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    # TODO: check if the text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=False)

