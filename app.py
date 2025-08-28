from flask import Flask , render_template,redirect,request,url_for

app = Flask(__name__)
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)
        
        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('hello_world'))
        except:
            return 'There was an issue adding your post'
    else:
        return render_template('create.html')
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'
#this is homepage route    
@app.route('/')
def hello_world():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about () :
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True)