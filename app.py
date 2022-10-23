
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

#route
@app.route('/')
def index():
    mylist = ['apple','oranges','banana']
    dict_profil = {"nama":"pulung","alamat":"antang","usia":"27"}
    return render_template('index.html',nama='andi',umur=90, list=mylist, mydict =dict_profil)


@app.route('/about/')
def about():
    return '<h1>About</h1>'


@app.route('/contact/')
def contact():
    return '<h1>Contact US</h1>'

@app.route('/profil/',defaults={'_route':"home",'nilai':0})
@app.route('/profil/<int:nilai>',defaults={'_route':"profil"})
def profil_name(nilai,_route):
    if _route == "home":
         return '<h1> Profil Home</h1>'
    elif _route == "profil":
        nilai =  nilai +1
        return '<h1>Hello %s </h1>' %nilai

@app.route('/cobarequest',methods=['GET','POST'])
def cobarequest():
    if request.method=="GET":
        #return "Coba GET"
        return "nama:"+request.args.get("nama")+" alamat:"+request.args.get("alamat")
    elif request.method=="POST":
        #return "Coba POST"
        return "nama:"+request.form["nama"]

#untuk menjalankan flask dan mode debug= isi file akan berubaha sesuai apa yang diedit secara realtime tanpa refresh server
#app.run(debug=True)
