from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"<h1>{parameter}</h1>"


@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter + 1))
    return f"<pre>{numbers}</pre>"


@app.route("/math/<int:num1><operation><int:num2>")
def math(num1, operation, num2):
    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2

    return f"<h1>Result: {result}</h1>"


if __name__ == "__main__":
    app.run()
