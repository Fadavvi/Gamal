# Hijacker-assist
A tiny flask app for helping pentesters and bug hunters in XSS, Session Hijacking, Session Riding and Cookie Thieve.

## Dependencies:
python 3
1. Flask
2. argparser !

## Install & usage:

```cd /opt```

```git clone github.com/Fadavvi/Hijacker-assist```

``` cd Hijacker-assist```

```python3 hijacker-assist.py```  run with default configuration (IP binding: 0.0.0.0, Port: 1337, Log: hijacker-assist.log)

or

```python3 hijacker-assist.py --ip <IPADDR> --port <PORTNUM> --log <LOGPATH>```

Then you can use your IP & Port into your payloads.

***IMPORTANT:*** add your JavaScript (or any other) file(s) in ```/js``` sub-directory and will avaliable on ```IP:PORT/js/<Your-File-Name>``` 

## Paylods:
```/js/1.js``` is a payload sample. (just change IP and Port)

More?
- Coming soon!
