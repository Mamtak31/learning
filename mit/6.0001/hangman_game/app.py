# from flask import Flask, request, redirect, session
# import random

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Sample questions
# questions = {
#     'animal': ['elephant', 'giraffe', 'kangaroo'],
#     'state': ['california', 'nevada', 'texas'],
#     'country': ['canada', 'brazil', 'india'],
#     'vegetable': ['carrot', 'broccoli', 'spinach']
# }

# def generate_html(content):
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Hangman Game</title>
#     </head>
#     <body>
#         {content}
#     </body>
#     </html>
#     """

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         category = request.form.get('category')
#         word = random.choice(questions[category])
#         session['word'] = word
#         session['guessed'] = ['_'] * len(word)
#         session['wrong_guesses'] = 0
#         return redirect('/game')
    
#     content = """
#     <h1>Welcome to Hangman Game</h1>
#     <form method="POST">
#         <label for="category">Choose a category:</label>
#         <select id="category" name="category">
#             <option value="animal">Animal Name</option>
#             <option value="state">State Name</option>
#             <option value="country">Country Name</option>
#             <option value="vegetable">Vegetable Name</option>
#         </select>
#         <button type="submit">Start Game</button>
#     </form>
#     """
#     return generate_html(content)

# @app.route('/game', methods=['GET', 'POST'])
# def game():
#     if request.method == 'POST':
#         char = request.form.get('char').lower()
#         word = session['word']
#         guessed = session['guessed']

#         if char in word:
#             for i, c in enumerate(word):
#                 if c == char:
#                     guessed[i] = char
#         else:
#             session['wrong_guesses'] += 1

#         session['guessed'] = guessed

#         if session['wrong_guesses'] >= 5:
#             message = "Game Over! Try next time."
#             return redirect(f'/result?message={message}')
#         elif '_' not in guessed:
#             message = f"Congratulations! You've guessed the word: {word}"
#             return redirect(f'/result?message={message}')
    
#     guessed = session['guessed']
#     wrong_guesses = session['wrong_guesses']
#     word_display = ' '.join(guessed)
#     image_url = f'/static/images/hangman{wrong_guesses}.png'
    
#     content = f"""
#     <h1>Hangman Game</h1>
#     <p>Word: {word_display}</p>
#     <p>Wrong Guesses: {wrong_guesses} / 5</p>
#     <form action="/game" method="post">
#         <label for="char">Guess a character:</label>
#         <input type="text" id="char" name="char" maxlength="1" required>
#         <button type="submit">Submit</button>
#     </form>
#     <img src="{image_url}" alt="Hangman Image">
#     """
#     return generate_html(content)

# @app.route('/result')
# def result():
#     message = request.args.get('message', 'Game Over!')
#     word = session['word']
    
#     content = f"""
#     <h1>{message}</h1>
#     <p>The word was: {word}</p>
#     <a href="/">Play Again</a>s
#     """
#     return generate_html(content)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample questions
questions = {
    'animal': ['elephant', 'giraffe', 'kangaroo'],
    'state': ['california', 'nevada', 'texas'],
    'country': ['canada', 'brazil', 'india'],
    'vegetable': ['carrot', 'broccoli', 'spinach']
}

def generate_html(content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hangman Game</title>
    </head>
    <body>
        {content}
    </body>
    </html>
    """

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form.get('category')
        word = random.choice(questions[category])
        session['word'] = word
        session['guessed'] = ['_'] * len(word)
        session['wrong_guesses'] = 0
        return redirect('/game')
    
    content = """
    <h1>Welcome to Hangman Game</h1>
    <form method="POST">
        <label for="category">Choose a category:</label>
        <select id="category" name="category">
            <option value="animal">Animal Name</option>
            <option value="state">State Name</option>
            <option value="country">Country Name</option>
            <option value="vegetable">Vegetable Name</option>
        </select>
        <button type="submit">Start Game</button>
    </form>
    """
    return generate_html(content)

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        char = request.form.get('char').lower()
        word = session['word']
        guessed = session['guessed']

        if char in word:
            for i, c in enumerate(word):
                if c == char:
                    guessed[i] = char
        else:
            session['wrong_guesses'] += 1

        session['guessed'] = guessed

        if session['wrong_guesses'] >= 4:
            message = "Game Over! Try next time."
            return redirect(f'/result?message={message}')
        elif '_' not in guessed:
            message = f"Congratulations! You've guessed the word: {word}"
            return redirect(f'/result?message={message}')
    
    guessed = session['guessed']
    wrong_guesses = session['wrong_guesses']
    word_display = ' '.join(guessed)
    image_url = f'/static/images/hangman{wrong_guesses}.png'
    
    content = f"""
    <h1>Hangman Game</h1>
    <p>Word: {word_display}</p>
    <p>Wrong Guesses: {wrong_guesses} / 4</p>
    <form action="/game" method="post">
        <label for="char">Guess a character:</label>
        <input type="text" id="char" name="char" maxlength="1" required>
        <button type="submit">Submit</button>
    </form>
    <img src="{image_url}" alt="Hangman Image">
    """
    return generate_html(content)

@app.route('/result')
def result():
    message = request.args.get('message', 'Game Over!')
    word = session['word']
    
    content = f"""
    <h1>{message}</h1>
    <p>The word was: {word}</p>
    <a href="/">Play Again</a>
    """
    return generate_html(content)

if __name__ == '__main__':
    app.run(debug=True)

