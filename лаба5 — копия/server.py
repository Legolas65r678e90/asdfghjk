from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
def index():
    return render_template("index.html")

def main():
    app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()