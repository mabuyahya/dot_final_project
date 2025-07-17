"""
flask
"""
"""flask is used for building dynamic web applications in Python."""
"""flask is a lightweight WSGI web application framework in Python."""
"""It is designed with simplicity and flexibility in mind, making it easy to get started with web development."""
"""Flask provides a simple and intuitive API for routing, request handling, and rendering templates."""

"""flask provide support for static routing and dynamic routing"""

"""the request {12.123.44.3/order/5}"""
"""the request file is a text file that contains the request information"""
"""first line of the request file : GET /order/5 HTTP/1.1"""
"""flask will parse the request file and extract the route path and send the request for the app.route()"""
"""also the route has a dynamic part, which is the order id in this case"""

"""the difference between dynamic routing and query parameters is that dynamic routing is used to capture a part of the URL as a variable, while query parameters are used to pass additional information in the URL."""

from flask import Flask, render_template # type:ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)