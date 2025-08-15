#!/usr/bin/python3

from flask import Flask, request, jsonify, send_from_directory
import json
import argparse
import ssl
import os
import uuid
from werkzeug.utils import secure_filename
############# Flask Routes #################
app = Flask(__name__,static_url_path='')
UploadPath = "received"
os.makedirs(UploadPath, exist_ok=True)
#------------------------------------------
@app.route('/info', methods=['GET','POST']) # Print info 
def info():
    return "<h3>Gamal v1.0.2 | Milad Fadavvi</h3>" 
#------------------------------------------
@app.route('/f/<path:path>') #Servs files
def send_js(path):
    return send_from_directory('f', path)
#------------------------------------------
@app.route("/e/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    # Save file to 'received' directory
    filepath = os.path.join(UploadPath, request.remote_addr + '-' + str(uuid.uuid1()) + '-' + file.filename)
    
    LogFile = open (Arguments.log, "a+")
    LogFile.write("-" * 33 + '\n')
    LogFile.write("URL: {} \n".format(request.url))
    LogFile.write("Requester: {} \n".format(request.remote_addr))
    LogFile.write("Method: {} \n".format(request.method))
    LogFile.write("Headers: [{}]\n".format(request.headers).replace('\r\n',' , '))
    
    try:
        LogFile.write("Get Args: {} \n".format(request.args.to_dict()))
        HostName = secure_filename(request.args.get('host',''))
        User = secure_filename(request.args.get('user',''))
        FileName = secure_filename(file.filename)
        UniqueName = f"{HostName}--{User}--{request.remote_addr}--{uuid.uuid4()}-{FileName}"
        filepath = os.path.join(UploadPath, UniqueName)
    except:
        pass

    if not os.path.abspath(filepath).startswith(os.path.abspath(UploadPath) + os.sep):
        return jsonify({"error": "Go Hack Yourself!"}), 400
    
    LogFile.close()
    file.save(filepath)

    return jsonify({"message": f"File uploaded successfully!"}), 200
#------------------------------------------
@app.errorhandler(404) 
@app.errorhandler(400)
@app.route('/<path:path>', methods=['GET','POST']) #Logs info
def SaveData(e='',path=''):
    LogFile = open (Arguments.log, "a+")
    LogFile.write("-" * 33 + '\n')
    LogFile.write("URL: {} \n".format(request.url))
    LogFile.write("Requester: {} \n".format(request.remote_addr))
    LogFile.write("Method: {} \n".format(request.method))
    LogFile.write("Path: {} \n".format(path))
    LogFile.write("Headers: [{}]\n".format(request.headers).replace('\r\n',' , '))
    try:
        LogFile.write("Get Args: {} \n".format(request.args.to_dict()))
    except:
        pass
    try:   
        LogFile.write("Post Args: {} \n".format(json.dumps(request.form.to_dict())))
    except:
        pass
    try:
        LogFile.write("JSON Data: {}\n".format(request.get_json()))
    except:
        pass
    LogFile.close()
    return '<html><b>{}</b></html>'.format(Arguments.canary) , 200
#------------------------------------------
############# Main Function ########################
if __name__ == "__main__":
    global Arguments #!!!
    #------------------------------------------
    parser = argparse.ArgumentParser(description='Gamal v1.0.2:\nA tiny flask app for helping pentesters, red-teamers and bug hunters in data exfileration, SSRF, XSS, Session Hijacking, Session Riding and Cookie Thieve.')
    parser.add_argument('--log', default='gamal.log' , help='Path to the log file')
    parser.add_argument('--port', default=1337 , help='Port / HTTPs')
    parser.add_argument('--ip', default='0.0.0.0' , help='IP e.g. : 0.0.0.0 or 127.0.0.1')
    parser.add_argument('--canary', default='booqbooqGamal' , help='Canary token')
    parser.add_argument('--cert', help='Your fullchain.pem file')
    parser.add_argument('--key', help='Your ssl private key file')
    Arguments = parser.parse_args()
    #------------------------------------------
    if Arguments.cert and Arguments.key:
        cert_file = Arguments.cert
        key_file = Arguments.key
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        app.run(host=Arguments.ip , port=int(Arguments.port),threaded=True, ssl_context=context)
    else: 
        try:
            app.run(host=Arguments.ip , port=int(Arguments.port),threaded=True, ssl_context='adhoc')
        except:
            parser.print_help()
