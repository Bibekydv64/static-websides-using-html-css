from flask import Flask,render_template,request,redirect,url_for,Response


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signin',methods = ['POST'])
def signin():
    name = request.form.get('username')
    password = request.form.get('password')

    if name == 'admain':
        if password == '123':
            return redirect(url_for('inner-home.html'))
        else:
            return Response(url_for('Invalid pass'))
    else:
        return Response(url_for('Invalid Email or usename'))



@app.route('/signup',methods = ['POST'])
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)