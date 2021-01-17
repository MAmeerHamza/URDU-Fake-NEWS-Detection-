from flask import Flask, redirect, url_for, render_template, request
import flask
app=flask.Flask(__name__,template_folder='templates')
@app.route('/')
@app.route('/Home')
def Home():
    return render_template("Home.html")
  
@app.route('',methods=['POST'])
def get_delay():

    result=request.form
  
    query_text = result['maintext']
    print(query_text)
    query = get_all_query(query_text)
    user_input = {'query':query}
   
if __name__ == '__main__':
    app.run(debug=True)