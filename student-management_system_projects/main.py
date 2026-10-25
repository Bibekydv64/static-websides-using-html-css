from flask import Flask, render_template,request,url_for,redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin-login', methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'bibek@12':
            if password == 'bibek':
                return redirect(url_for('admin_dashboard'))
            else:
                return 'Invalid Password! try again'
        else:
            return 'invalid name! try agin'
        
    return render_template('login_admin/login-admin.html')



@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('dashboard_page/dashboard.html')

@app.route('/add-student')
def add_student():
    return render_template('dashboard_page/add-student.html')


if __name__ == "__main__":
    app.run(debug=True)
