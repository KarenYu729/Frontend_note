from flask import Flask, render_template, request

app = Flask(__name__)

"""
# can only use GET request
# because register.html -> form
# if submit, data in the form will appeared in URL (str concat)
@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/post/register', methods=['GET'])
def post_register():
    return render_template("post_register.html")

@app.route('/done/register', methods=['GET'])
def done_register():
    print(request.args)
    return "done register"
    # return render_template('done_register.html')

@app.route('/done/Pregister', methods=['POST'])
def done_Pregister():
    print(request.form)
    user = request.form.get("user")
    psw = request.form.get("psw")
    gender = request.form.get("gender")
    city = request.form.get("city")
    team = request.form.get("user")
    comment = request.form.get("addText")
    print(user, psw)
    print(team, city)
    print(gender)
    return "done post register"
    # return render_template('done_Pregister.html')
"""
@app.route('/combRegister', methods=['GET', 'POST'])
def combRegister():
    if request.method == "GET":
        return render_template("post_register.html")
    else:
        print(request.form)
        user = request.form.get("user")
        psw = request.form.get("psw")
        gender = request.form.get("gender")
        city = request.form.get("city")
        team = request.form.get("user")
        comment = request.form.get("addText")
        print(user, psw)
        print(team, city)
        print(gender)
        return "done post register"

if __name__ == '__main__':
    app.run()