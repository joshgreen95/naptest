# Naptest- Not Another Pentest
This is (probably) the world's most awful pentest automation script. It does many things to just create a bash script which runs GNU parallel.

## Usage:

```
$ python naptest -h
usage: naptest [-h] {scope,scan,parse,status,test} ...

positional arguments:
  {scope,scan,parse,status,test}
                        sub-command help
    scope               scope mode will create a list of IPs from a list of ranges.
    scan                scan mode will attempt to identify and scan in scope hosts. By default it will arp-scan any local IPs, perform an nmap host discovery
                        scan, and then a top20 port TCP scan.
    parse               parse mode will generate output based on completed nmap scans.
    status              status mode will show you the status of nmap scans.
    test                test mode runs pre-defined tools against the identified services in scope.

options:
  -h, --help            show this help message and exit


$ python naptest scope -h
usage: naptest scope [-h] [-p] [-o OUTPUT] [-e EXCLUDE] [-a] input

positional arguments:
  input                 File containing scope

options:
  -h, --help            show this help message and exit
  -p, --print           Print the IPs in scope
  -o OUTPUT, --output OUTPUT
                        directory for output
  -e EXCLUDE, --exclude EXCLUDE
                        IPs to exclude. Comma separated.
  -a, --autoexclude     Automatically exclude all your IPs (from all interfaces).


$ python naptest scan -h
usage: naptest scan [-h] [-o OUTPUT] [-p PARALLEL] [--no-discovery]

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        directory for output
  -p PARALLEL, --parallel PARALLEL
                        number of scans to run in parallel
  --no-discovery        skip discovery scans and fully nmap scan every in scope address

$ python naptest parse -h
usage: naptest parse [-h] [-o OUTPUT] xml

positional arguments:
  xml                   directory containing nmap output

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        directory for output


$ python naptest status -h
usage: naptest status [-h] directory

positional arguments:
  directory   directory containing nmap output

options:
  -h, --help  show this help message and exit


$ python naptest test -h
usage: naptest test [-h] [-o OUTPUT] [-c] directory

positional arguments:
  directory             directory containing the services.array

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        directory for output
  -c, --check           checks if all tools are available in $PATH

```


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
