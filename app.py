import random
from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "saiket-number-guessing-secret"

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Number Guessing Game</title>
<style>
  * { box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #0d1117;
    color: #e6edf3;
    display: flex;
    justify-content: center;
    padding: 40px 15px;
    margin: 0;
  }
  .card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 30px;
    width: 100%;
    max-width: 420px;
    text-align: center;
  }
  h1 { font-size: 22px; color: #58a6ff; margin-bottom: 10px; }
  p.sub { color: #8b949e; font-size: 14px; margin-bottom: 20px; }
  input {
    width: 100%;
    padding: 12px;
    border-radius: 6px;
    border: 1px solid #30363d;
    background: #0d1117;
    color: #e6edf3;
    font-size: 16px;
    text-align: center;
    margin-bottom: 15px;
  }
  button {
    width: 100%;
    padding: 12px;
    background: #238636;
    color: #fff;
    border: none;
    border-radius: 6px;
    font-size: 15px;
    cursor: pointer;
  }
  button:hover { background: #2ea043; }
  .message {
    margin-top: 18px;
    padding: 14px;
    border-radius: 8px;
    font-size: 15px;
  }
  .hint { background: #1c2128; color: #d29922; border: 1px solid #30363d; }
  .win { background: #0f2e1a; color: #3fb950; border: 1px solid #238636; }
  .guesses { margin-top: 10px; color: #8b949e; font-size: 13px; }
  a.reset {
    display: inline-block;
    margin-top: 16px;
    color: #58a6ff;
    font-size: 13px;
    text-decoration: none;
  }
</style>
</head>
<body>
  <div class="card">
    <h1>🎯 Number Guessing Game</h1>
    <p class="sub">Guess a number between 1 and 100</p>

    <form method="POST">
      <input type="number" name="guess" placeholder="Enter your guess" min="1" max="100" required autofocus>
      <button type="submit">Submit Guess</button>
    </form>

    {% if message %}
      <div class="message {{ 'win' if won else 'hint' }}">{{ message }}</div>
    {% endif %}

    <div class="guesses">Attempts so far: {{ attempts }}</div>

    <a class="reset" href="/reset">🔄 Start New Game</a>
  </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if "target" not in session:
        session["target"] = random.randint(1, 100)
        session["attempts"] = 0

    message = None
    won = False

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            session["attempts"] += 1

            if guess < session["target"]:
                message = f"📈 Too low! Guess higher than {guess}."
            elif guess > session["target"]:
                message = f"📉 Too high! Guess lower than {guess}."
            else:
                message = f"🎉 Correct! The number was {session['target']}. You took {session['attempts']} attempts!"
                won = True
                session.pop("target", None)
        except (ValueError, KeyError):
            message = "Please enter a valid number between 1 and 100."

    attempts = session.get("attempts", 0)
    return render_template_string(PAGE, message=message, won=won, attempts=attempts)


@app.route("/reset")
def reset():
    session.pop("target", None)
    session.pop("attempts", None)
    return index()


if __name__ == "__main__":
    app.run(debug=True)
