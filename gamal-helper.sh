#!/usr/bin/env bash
####################################################
sudo apt install p7zip-full wget curl -y
cd f
mkdir --parents win linux mac

cd win

wget --quiet https://github.com/gentilkiwi/mimikatz/releases/latest/download/mimikatz_trunk.zip
7z x mimikatz_trunk.zip -o./mimikatznk > /dev/null
mv mimikatz_trunk/x64/ mimikatz64
rm -rf mimikatz_trunk/ mimikatz_trunk.zip

wget --quiet https://github.com/Flangvik/SharpCollection/archive/refs/heads/master.zip
7z x master.zip > /dev/null
mv SharpCollection-master/NetFramework_4.7_x64 sharpc64
rm -rf SharpCollection-master master.zip

curl -s https://api.github.com/repos/nicocha30/ligolo-ng/releases/latest | grep "browser_download_url.*windows_amd64*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
for /r %f in (*.zip) do 7z x %f -o*
mkdir --parents ligolo
mv ligolo-ng_agent*/agent.exe ligolo/agent.exe
mv ligolo-ng_proxy*/proxy.exe ligolo/proxy.exe
rm -rf ligolo-ng_agent* ligolo-ng_proxy*

curl -s https://api.github.com/repos/peass-ng/PEASS-ng/releases/latest | grep "browser_download_url.*winPEAS*" | cut -d : -f 2,3 | tr -d \" | wget -qi -
mkdir --parents peass
mv winPEAS* peass