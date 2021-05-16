from flask import Flask, redirect, url_for, render_template, request, session, flash
import os

app = Flask(__name__)

app.secret_key = 'hello'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    return render_template('thankyou.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/pizza')
def pizza():
    return render_template('pizza.html')


@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == "GET":
        return render_template('order.html')
    elif request.method == "POST":
        data = request.form
        order = dict(data)
        print(order)
        check_order = []
        for key in order:
            check_order.append(order[key])
        delivery_type = check_order[0]
        address = check_order[1]
        city = check_order[2]
        state = check_order[3]
        zipcode = check_order[4]
        size = check_order[5]
        print(delivery_type)
        print(address)
        print(city)
        print(zipcode)
        print(size)
        list_order = str(check_order)
        # Determine incremented filename
        i = 0
        while os.path.exists(f"orders/order_{i}.txt"):
            i += 1
        file = open(f"orders/order_{i}.txt", "w")
        file.write(list_order)
        file.close()
        return render_template('order.html')
        # return render_template('checkout.html', data=data, delivery_type=delivery_type, address=address, city=city, state=state, size=size, zipcode=zipcode, ingredients=ingredients)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
