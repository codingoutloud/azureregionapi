from flask import Flask
from flask import render_template
from flask import jsonify, request
from azureip import AzureIp

app = Flask(__name__)
azure_ip = AzureIp()


@app.route('/')
def home():
    text = { 'content': 'Welcome to your flask application !' } 
    return render_template("home.html",
        title = 'Home',
        text = text)


@app.route('/regions/<ip_address>', methods=["GET"])
def get_region(ip_address):
    region = azure_ip.find_ip(ip_address)
    if region is None:
        return jsonify(region='<unknown>'), 404
    else:
        return jsonify(region=region)


app.debug = True
app.debug = False
if __name__ == "__main__":
    app.run()

