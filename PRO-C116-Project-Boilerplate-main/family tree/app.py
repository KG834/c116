# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Kaan" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/a")
def first_website():
    return render_template('father.html', name = "Sinan", age = 43)

# define the route to mother webpage
@app.route("/b")
def second_website():
    return render_template('mother.html', name = "Ekin", age = 41)

# define the route to friends webpage
@app.route("/c")
def third_website():
    return render_template('friend.html', name = "Ethan", age = 13)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
