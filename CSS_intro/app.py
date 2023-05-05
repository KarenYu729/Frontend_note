from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def log_in():
    return render_template("log_in.html")

if __name__ == '__main__':
    app.run()