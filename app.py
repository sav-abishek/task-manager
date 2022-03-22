from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# // Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
# // TODO: Add SDKs for Firebase products that you want to use
# // https://firebase.google.com/docs/web/setup#available-libraries

# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC_Ag8lqcvHHZ9HjjT1YfEJQ-MhYtY2Ikk",
  authDomain: "task-manager-72d02.firebaseapp.com",
  projectId: "task-manager-72d02",
  storageBucket: "task-manager-72d02.appspot.com",
  messagingSenderId: "772192900755",
  appId: "1:772192900755:web:b844d39e8ca8e64e591f66",
  measurementId: "G-QGS3GSQ482"
};

# // Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///task.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default = datetime.utcnow)



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error in adding your task"

    else:
        tasks = todo.query.order_by(todo.created).all()
        return render_template("index.html", tasks = tasks)

    

@app.route('/update')
def hi():
    return "hi"

@app.route('/delete/<int:id>')
def delete(id):
    task = todo.query.get(id)

    db.session.delete(task)
    db.session.commit()
    return redirect('/')
   

if __name__ == "__main__" :
    app.run()