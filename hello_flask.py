from flask import Flask

app = Flask(__name__)

def search4letters(text, letters='aeiou') -> set:
    output = set()
    for i in text:
        if i in letters:
            output.add(i)
    return output

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the unvierse, and everything', 'eiru,!'))

app.run()