from flask import Flask, request, render_template, redirect, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        data = (requests.get(
            'https://api.exchangerate.host/symbols').json())['symbols'].keys()
        return render_template('index.html', data=data)
    elif request.method == "POST":
        convert_from = request.form.get("convert-from")
        convert_to = request.form.get("convert-to")
        convert_amount = request.form.get("convert-amount")
        try:
            data = round((requests.get(
                f'https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={convert_amount}').json())['result'], 2)
        except TypeError:
            flash(f'Cannot convert {convert_from} to {convert_to}')
            print(f'Cannot convert {convert_from} to {convert_to}')
        else:
            flash(
                f'{convert_amount} {convert_from} converts to {data} {convert_to}', 'success')
        finally:
            return redirect('/')


app.run(debug=True)
