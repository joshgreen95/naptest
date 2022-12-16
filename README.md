# Naptest- Not Another Pentest
This is (probably) the world's most awful pentest automation script. It does many things to just create a bash script which runs GNU parallel.

## Usage:

`$ python naptest generate <nmap XML file/folder containing nmap XML files> #Generates the services db/array/flat files from nmap`
`$ python testgen.py #Needs the services.array from the above command`
`$ bash CABO.sh #Congrats, you have pentested`

## Features
* Idempotence
* Handles broken/cancelled scan output (by ignoring it)
* Flags closed ports (remember -dd for nmap)
* Uses hostnames for SSL/HTTP/HTTPS
* Will ingest nmap script output to the database. Currently no output.

## Output
* naptest.db- a sqlite database with openports,closedports,hostnames and scripts tables.
* services.array- a python object containing all the open ports identified.
* services/{tcp,udp}/<services>- a file structure containing useful text files for running tools against
