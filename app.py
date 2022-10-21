from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__) # we created new OBJECT
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# db = SQLAlchemy(app)

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     intro = db.Column(db.String(300), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self): # це означає що коли ми будемо вибирати будь який обєкт на основі цього класу то у нас буде видаватися нам сам обєкт і + буде видаватися його id
#         return '<Article %r>' % self.id


@app.route('/') # тут ми вказуємо що виконувати якщо запуститься та чи інша сторінка, в даному випадук '/' - це головна сторінка. А якби було '/about' - це сторінка about
@app.route('/home')
def index():
    return render_template('index.html')
    # return 'Hello Mikle'
    # return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html')
    # return 'About me'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + ' - ' + str(id)


if __name__ == '__main__': #тут ми квазуємо, що якщо ми запускаємо наш проект через цей основний файл app.py, тоді виконається запуск програми
    app.run(debug=True)  # debug=True означає щоб виводились всі помилки на екран, якщо ми захочемо їх сховати далі то змінимо True на False


#app = Flask(__name__, template_folder='templates')