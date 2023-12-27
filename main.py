# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import app
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from basic_calculator_function import basic_calculator


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = basic_calculator(a, b, operation)

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
