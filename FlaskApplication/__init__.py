import os
import logging
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import jsonify, request
from azureip import AzureIp

app = Flask(__name__)
azure_ip = AzureIp()
simple_counter = 0

# assumes import os and import logging
# pass in root folder where logging is allowed (correct permissions are assumed)
# returns log_file_path
def init_logging(plat_root_log_dir):
    log_level = logging.DEBUG
    log_file_dir = os.path.join(plat_root_log_dir, 'azureregionapi-logs')
    log_file_path = os.path.join(log_file_dir, 'azregapi.log')

    log_file_dir_already_exists = os.path.exists(log_file_dir)
    if not log_file_dir_already_exists:
        os.makedirs(log_file_dir)

    logging.basicConfig(format='%(levelname)s [%(asctime)s]: %(message)s', filename=log_file_path, level=log_level)

    if not log_file_dir_already_exists:
        logging.info('Created %s logging directory', log_file_dir)
    logging.info('Flasky is logging to %s at level %s', log_file_path, log_level)
    return log_file_path

plat_root_log_dir = 'd:\\home\\logfiles'
log_file_path = init_logging(plat_root_log_dir)


@app.route('/')
def home():
    global simple_counter
    logging.debug('hello #%d from COMPUTERNAME = %s to visiting IP = %s', 
        simple_counter, os.getenv('COMPUTERNAME', 'unknown'), request.remote_addr)
    simple_counter += 1

    region = azure_ip.find_ip(request.remote_addr)
    if region is None: region = "<unknown>"
    text = { 
        'ip': request.remote_addr,
        'region': region,
        'timestamp': datetime.now()
        }
         
    return render_template("home.html",
        title = 'Azure Region API - Main',
        text = text)


@app.route('/regions/<ip_address>', methods=["GET"])
def get_region(ip_address):
    global simple_counter
    logging.debug('hello #%d from COMPUTERNAME = %s to visiting IP = %s', 
        simple_counter, os.getenv('COMPUTERNAME', 'unknown'), request.remote_addr)
    simple_counter += 1

    region = azure_ip.find_ip(ip_address)
    if region is None:
        return jsonify(region='<unknown>'), 404
    else:
        return jsonify(region=region)

app.debug = True
#app.debug = False
print("__name__ = %s" % __name__)
if __name__ == "__main__":
    print("running flask server -- debug = %r" % app.debug)
    app.run()

