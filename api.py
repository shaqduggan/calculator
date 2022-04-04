"""api.py"""
from flask import Flask, jsonify, request, render_template


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
def is_valid_expression(expression):
    """Checks if Valid Operator is present in string"""
    op_list = ['+','-','*','x','/','//','%']
    for operator in op_list:
        if operator in expression:
            return True
    return False


@server.route("/evaluate/<string:expr>", methods=["GET"])
def evaluate(expr: str):

    if is_valid_expression(expr):

        try:
            res = eval(expr)
        except Exception as an_error:
            raise an_error

        return jsonify({"result": res})



if __name__ == '__main__':
    server.run("0.0.0.0", debug=True)
