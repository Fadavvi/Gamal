# Gamal
A tiny flask app for helping pentesters and bug hunters in XSS, Session Hijacking, Session Riding and Cookie Thieve.

## Dependencies:
python 3
1. Flask

## Install & usage:

```cd /opt```

```git clone github.com/Fadavvi/Gamal```

```cd Gamal```

```python3 gamal.py```  
Default configuration: IP binding: `0.0.0.0`, Port: `1337`, Log: `gamal.log`, Canary-String: `BooqBooqGamal`

or

```python3 gamal.py --ip <IPADDR> --port <PORTNUM> --log <LOGPATH> --canary <YourCanaryString>```

Then you can use your IP & Port in your XSS | XXE | Open-Redirect | Etc. payloads

***Note:*** Add your files in ```/f``` folder ==>  ```http://IP:PORT/f/<Your-FileName>``` 

## Paylods:
```/f/xss.js``` XSS Sample function

```/f/CORS.html``` CORS sample script

```/f/CSRF.html``` CSRF sample page

```/f/CSWSH.html``` Cross-Site WebSocket Hijacking (CSWSH) script

```/f/meta.jpg``` XSS in Meta-data 

```/f/EBXXE.dtd``` XXE .dtd sample file

```/f/xxe1.svg``` and ```/f/xxe2.svg``` XXE in SVG file
