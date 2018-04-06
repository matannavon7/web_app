#! /usr/bin/env python
from flask import Flask, render_template
app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
@app.route("/")
def main():
    return render_template('index.html')

    return render_template('index_2.html')

if __name__ == "__main__":
    # app.run(host='192.168.1.100')
    app.run()

