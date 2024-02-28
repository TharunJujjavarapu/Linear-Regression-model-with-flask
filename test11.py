from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def greet():
    return('hello')

@app.route('/tharun')
def greet1():
    return('Good morning')

@app.route('/gowtham',methods=['Get'])
def greet2():
    n1=10
    n2=20
    return([n1+n2])

@app.route('/addition2',methods=["Get"])
def addition2():
    num1=request.args.get("num1")
    num2=request.args.get("num2")
    return([int(num1)+int(num2)])

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)