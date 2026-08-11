# Task 4: Number Guessing Game

**Internship:** Software Development | SaiKet Systems
**Stack:** Python (Flask), HTML/CSS
**Live Demo:** *(add your Vercel URL here after deployment)*

## Overview
A web-based number guessing game where the computer picks a random number between 1 and 100, and the user tries to guess it — receiving real-time "too high" / "too low" hints after every attempt, with the total number of guesses tracked until the correct answer is found.

## Objective
Develop a simple game where the computer selects a random number between 1 and 100, and the user must guess it, receiving hints until they guess correctly.

## Features
- Random number generation (1–100) using Python's `random` module
- Real-time hints: "Too high" 📉 / "Too low" 📈
- Session-based state — each visitor gets their own independent game via Flask sessions
- Tracks and displays total number of attempts taken
- Congratulatory message with final attempt count on correct guess
- Input validation (rejects non-numeric or out-of-range guesses)
- One-click "Start New Game" to reset and play again
- Clean, responsive dark-themed UI — works great on mobile

## How It Works
- On first visit, a random target number (1–100) is generated and stored in the Flask session
- Each guess is submitted via a POST request; the app compares it to the target and returns a hint
- Attempt count persists in the session until the number is guessed correctly or the game is reset
- `/reset` route clears the session and starts a fresh round

## Tech Stack
- Python 3 + Flask
- Flask sessions for per-user game state
- HTML/CSS (inline templating via `render_template_string`)

## Deployment
Deployed on **Vercel** using the `@vercel/python` runtime.

## How to Run Locally
```bash
pip install -r requirements.txt
python app.py
```
Then open `http://localhost:5000` in your browser.

## Project Files
- `app.py` — Flask application (game logic + UI)
- `requirements.txt` — Python dependencies
- `vercel.json` — Vercel deployment configuration

## Requirements
- Python 3.x
- Flask (`pip install -r requirements.txt`)

## Learning Outcomes
- Building interactive web apps with Flask
- Managing per-user state using server-side sessions
- Handling form submissions and input validation
- Deploying Python web apps on Vercel

---
*Part of the Software Development Internship Program at SaiKet Systems*
