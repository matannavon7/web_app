#! /usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run(host='192.168.1.100')

