from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return (f"{self.sno} - {self.title}")


@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "POST":
        title_ = request.form['title']
        desc_ = request.form['desc']
        todo = Todo(title=title_, desc=desc_)
        db.session.add(todo)
        db.session.commit()
        #return redirect("http://127.0.0.1:8001/")
        return redirect("/")   # updated for Render


    allTodo = Todo.query.all()
    print(allTodo)
    #return "Hello, Flask! Your setup is working 🎉"
    return render_template('index.html', allTodo = allTodo)

@app.route("/show")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'

@app.route("/update/<int:sno>", methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title_ = request.form['title']
        desc_ = request.form['desc']
        todo =  Todo.query.filter_by(sno=sno).first()
        todo.title = title_
        todo.desc = desc_
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)
     

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


# given by sir while working with heroku
# if __name__ == "__main__":  
#     app.run(debug=True, port = 8001)


if __name__ == "__main__":
    db.create_all() 