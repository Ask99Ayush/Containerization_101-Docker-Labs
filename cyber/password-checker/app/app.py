from flask import Flask, render_template, request

app = Flask(__name__)

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in "!@#$%^&*" for char in password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def home():
    strength = None

    if request.method == "POST":
        password = request.form.get("password")
        strength = check_strength(password)

    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)