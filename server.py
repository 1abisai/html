from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def user():
    users = [
   {'first_name1' : 'Michael', 'last_name1' : 'Choi'},
   {'first_name2' : 'John', 'last_name2' : 'Supsupin'},
   {'first_name3' : 'Mark', 'last_name3' : 'Guillen'},
   {'first_name4' : 'KB', 'last_name4' : 'Tonel'}
]
    return render_template('index.html', users=users)

if __name__=="__main__":
    app.run(debug=True)