from flask import Flask, jsonify, request
from azureip import AzureIp

app = Flask(__name__)
azure_ip = AzureIp()


@app.route('/', methods=["GET"])
def hello_world():
    return 'Hello from the Azure Region API'


@app.route('/myregion', methods=["GET"])
def show_region_for_ambient_ip_address():
    ip_address = request.remote_addr
    region = azure_ip.find_ip(ip_address)
    return 'You appear to be from IP address %s which is in region %s' % (ip_address, region)


@app.route('/regions/<ip_address>', methods=["GET"])
def get_region(ip_address):
    region = azure_ip.find_ip(ip_address)
    if region is None:
        return jsonify(region='<unknown>'), 404
    else:
        return jsonify(region=region)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()

