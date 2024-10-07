#!/bin/python3
# Craft, Artisanal, Bespoke, Organic pentest script generator

import sys,os,argparse,ast
from shutil import which
testlist="./testlist"
servicearrayfile="./services.array"
modulepath=str(os.path.dirname(os.path.realpath(__file__)))+"/modules/"
queuefile="CABO.sh"
mkdirqueue=[]
cmdqueue=[]
invalid_commands = []

def parsefile(infile):
    with open(infile) as f:
        response = ast.literal_eval(f.read())
        return response

servicearray = parsefile(servicearrayfile)

for service in servicearray:
    tests=""
    if os.path.exists(modulepath+service):  
        try:
            tests=parsefile(modulepath+service)
            print(("[+] Found tests for "+service))
        except Exception as e:
            print("[!] Error processing "+service+" module: "+str(e))

    for test in tests:
        testlist=tests[test]
        testtype=testlist[0]
        outputfolder=testlist[1]
        testcommand=testlist[2]
        testprotocol=testlist[3]
        testexe = testcommand.split(" ")[0]
        exe = which(testexe)
        interpreters = ['perl','python']
        
        if exe is None:
            invalid_commands.append(test)

        if exe is not None and exe.split("/")[-1] in interpreters:
            print("[!] Interpreter detected for "+test+". Make sure the script exists.")
        
        if exe is not None:
            print(("[*] Adding "+test+" to the queue"))
            mkdirqueue.append("mkdir "+outputfolder)    
            for host in servicearray[service][testprotocol]:
                if service == "plainhttp":
                    proto="http"
                elif service == "securehttp":
                    proto="https"
                else:
                    proto="tcp"
                hostip=host.split(":")[0]
                hostport=host.split(":")[1]
                
                towriteout=str(testcommand)
                towriteout=towriteout.replace("DIR", outputfolder)
                towriteout=towriteout.replace("HOST", host)
                towriteout=towriteout.replace("IP", hostip)
                towriteout=towriteout.replace("PORT", hostport)
                towriteout=towriteout.replace("PROTO", proto)
                cmdqueue.append(towriteout)


with open(queuefile, "w") as f:
    f.write("#!/bin/parallel --shebang\n")
    for line in mkdirqueue:
        f.write(line+"\n")
    for line in cmdqueue:
        f.write(line+"\n")
    if invalid_commands:
        print("[!] The following commands could not be found, and have not been added to the script:\n"+",".join(invalid_commands))

