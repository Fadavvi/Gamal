#!/usr/bin/env bash
####################################################
echo "Run 'sudo apt install p7zip-full wget curl -y' first!"
####################################################
cd f
mkdir --parents win linux mac web
####################################################
cd win

wget --quiet https://github.com/gentilkiwi/mimikatz/releases/latest/download/mimikatz_trunk.zip
7z x mimikatz_trunk.zip -o./mimikatznk &> /dev/null
mv mimikatznk/x64/ mimikatz64
rm -rf mimikatznk/ mimikatz_trunk.zip

wget --quiet https://github.com/Flangvik/SharpCollection/archive/refs/heads/master.zip
7z x master.zip > /dev/null
mv SharpCollection-master/NetFramework_4.7_x64 sharpc64
rm -rf SharpCollection-master master.zip

curl -s https://api.github.com/repos/nicocha30/ligolo-ng/releases/latest | grep "browser_download_url.*windows_amd64*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
find . -type f -name "*.zip" -exec 7z x {} -o* \;
mkdir --parents ligolo
mv ligolo-ng_agent*/agent.exe ligolo/agent.exe
mv ligolo-ng_proxy*/proxy.exe ligolo/proxy.exe
rm -rf ligolo-ng_agent* ligolo-ng_proxy*

curl -s https://api.github.com/repos/peass-ng/PEASS-ng/releases/latest | grep "browser_download_url.*winPEAS*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mkdir --parents peass
mv winPEAS* peass

curl -s https://api.github.com/repos/SpecterOps/AzureHound/releases/latest | grep "browser_download_url.*windows_amd64*" | cut -d : -f 2,3 | tr -d \" | head -n 1 | wget -qi -
7z x AzureHound*.zip
rm -f AzureHound*.zip

wget --quiet https://nmap.org/dist/ncat-portable-5.59BETA1.zip
7z x ncat-portable-5.59BETA1.zip
mv ncat-portable-5.59BETA1/ncat.exe .
rm -rf ncat-portable-5.59BETA1

####################################################
cd linux

curl -s https://api.github.com/repos/peass-ng/PEASS-ng/releases/latest | grep "browser_download_url.*linpeas_linux*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mkdir --parents peass
mv linpeas* peass
curl -s https://api.github.com/repos/peass-ng/PEASS-ng/releases/latest | grep "browser_download_url.*linpeas*.sh" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mv linpeas* peass

curl -s https://api.github.com/repos/nicocha30/ligolo-ng/releases/latest | grep "browser_download_url.*linux_amd64*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mkdir --parents ligolo
find . -type f -name "*.tar.gz" -exec tar -xvf {} -C ligolo \;
rm -f ligolo/README.md ligolo/LICENSE

curl -s https://api.github.com/repos/SpecterOps/AzureHound/releases/latest | grep "browser_download_url.*linux_amd64*" | cut -d : -f 2,3 | tr -d \" | head -n 1 | wget -qi -
7z x AzureHound*.zip
rm -f AzureHound*.zip

curl -s https://api.github.com/repos/liamg/traitor/releases/latest | grep "browser_download_url.*amd64*" | cut -d : -f 2,3 | tr -d \" | wget -qi -


####################################################
cd mac

curl -s https://api.github.com/repos/peass-ng/PEASS-ng/releases/latest | grep "browser_download_url.*darwin_amd64" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mkdir --parents peass
mv linpeas* peass

curl -s https://api.github.com/repos/nicocha30/ligolo-ng/releases/latest | grep "browser_download_url.*darwin_amd64.tar.gz" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mkdir --parents ligolo
find . -type f -name "*.tar.gz" -exec tar -xvf {} -C ligolo \;
rm -f ligolo/README.md ligolo/LICENSE ligolo-ng*.tar.gz

curl -s https://api.github.com/repos/SpecterOps/AzureHound/releases/latest | grep "browser_download_url.*darwin*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
7z x AzureHound*.zip
rm -f AzureHound*.zip

####################################################
cd web

curl -s https://raw.githubusercontent.com/BlackArch/webshells/refs/heads/master/asp/cmdasp.asp -o cmdasp.asp
curl -s https://raw.githubusercontent.com/BlackArch/webshells/refs/heads/master/aspx/cmdasp.aspx -o cmdasp.aspx
curl -s https://raw.githubusercontent.com/BlackArch/webshells/refs/heads/master/jsp/cmdjsp.jsp -o cmdjsp.jsp 
curl -s https://raw.githubusercontent.com/BlackArch/webshells/refs/heads/master/php/pws.php -o cmdphp.php
