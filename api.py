"""api.py"""
from flask import Flask, jsonify, request, render_template  
from calculator import Calculator
import os

# OUR WEBSITE

server = Flask(__name__)
@server.route("/", methods=['Get','Post'])
def index():
    """
    main page 
    """

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        math_sign_operator = request.form['op']
              
        if math_sign_operator == "+":
            res = (num1 + num2)

        elif math_sign_operator == "-":
            res = (num1 - num2)

        elif math_sign_operator == "*" or math_sign_operator == "x":
            res = (num1 * num2)
        
        elif math_sign_operator == "/" and num2 > 0:
            res = (num1 / num2)

        elif math_sign_operator == "%" and num2 > 0:
            res = (num1 % num2)
            
        else:
            res = "Invalid operator"

        # print(type(res))
        return render_template("index.html",res = res)

    else:
        return render_template("index.html")



# OUR API

@server.route("/evaluate/<string:expr>", methods=["GET"])
def evaluate(expr: str):

	# if is_valid_expression():
	# 	pass

	try:
		res = eval(expr)
	except Exception as e:
		raise e

	return jsonify({"result": res})



if __name__ == '__main__':
	server.run("0.0.0.0", debug=True)
