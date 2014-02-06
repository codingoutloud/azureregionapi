from flask import Flask
from flask import render_template
from flask import jsonify, request
from azureip import AzureIp

app = Flask(__name__)
azure_ip = AzureIp()


@app.route('/')
def home():
	ip_address = request.remote_addr
    text = { 'content': 'Welcome to your flask application from IP address %s!' % ip_address = ip_address } 
    return render_template("home.html",
        title = 'Home',
        text = text)
    ip_address = request.remote_addr
    #region = azure_ip.find_ip(ip_address)
    #return 'You appear to be from IP address %s which is in region %s' % (ip_address, region)


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

