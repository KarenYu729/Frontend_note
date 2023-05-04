from flask import Flask, render_template

app = Flask(__name__)

# /show/info <-> index() function
# when visit /show/info, index() function .exe
@app.route("/show/info")
def index():
    # flask will find the file named "index.html and return value in this file
    # which direction will flask check?
    # default: in the folder named "templates" in the project folder
    return render_template("index.html")

@app.route('/get/news')
def get_news():
    return render_template("get_news.html")

@app.route('/birds/list')
def birds_list():
    return render_template("birds_list.html")

@app.route('/birds/table')
def birds_table():
    return render_template("birds_table.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run()