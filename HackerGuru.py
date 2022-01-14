#!/bin/python3
## This is a fun script to generate random answer to hacking related questions. If you or someone you know want to know how to hack something, you can just consult this script for an answer :)
# How to extend:
# 	Extending this script with additional terms and senteces is easy, but some things need be known:
# 		If you want to add a term, for instance a new website, just add it to the list. Elements in 'target' need a leading space, so the sentences look correct. It is " the URL" not "the URL"
# 		If you want to add a sentence, add it and don't forget to increate the argument of random.randrange(), so that your new option can be chosen.


# Check if the user actually asked a question
import sys
if (len(sys.argv)==1):
	input=input("What do you want to know? ")
else:
	input=str(sys.argv[1])
# help does not work yet
#if (input.split(' ',1)[0] != "--help"):
#	print("type: 'python3 HackerGuru.py How do I hack the internet?' to get answers.")
#	sys.exit(0)
if (input.split(' ',1)[0] != "How" and input.split(' ',1)[0] != "how"):
	print("You question needs to start with the word 'How'.")
	sys.exit(0)

import random

# returns random entry from list
def get_random(list):
	return list[ random.randrange(len(list)) ]

### Ressources for the sentence generation

## list of terms, can easily be extended, just mind the spacing if there is any
# list of tools
tool=["BurpSuit","JohntheRipper","Nmap","Nessus","Recon-ng","Nmap","NetBIOS","Nessus","L0phtCrack","njRAT","Wireshark","SET","HOIC","ZAP","sqlmap","Aircrack-ng","Kiuwan","Netsparker","Nikto","Burp","John","Angry","Metasploit","Ettercap","SocialEngineering","a reverse shell","a bind shell","bruteforce"]

# list of actions
action=["hack","penetrate","crack","reverseengineer","bruteforce","socialengineer","root"]

# list of protocols
protocol=["FTP","SSH","Telnet","SMTP"," NS","HTTP","POP3","NNTP","NTP","IMAP","SNMP","IRC","HTTPS"]

# list of websites
website=["Google","Facebook","Youtube","Instagram"]

# list of targets
target=[" the server", " the IP Adress", " the URL", " the Website", " everything", " the NSA", " the government"]
# any ports can be a target
for i in protocol:
	target.extend([" the " + i + " protocol"])
	target.extend([" the " + i + " port"])
# any website can be a target
for i in website:
	target.extend([" the " + i + " Account"])
	target.extend([" " + i])

# list of sencente endings
end=[".","?"," :)"]

# get a common combination of action and target
def get_purpose():
	return " to " + get_random(action) +  get_random(target)

# followup is checked to see wether a second sentence shall be appended
followup=True

### Actual sentence generation

## choose a random first sentence
# the random selection happens via the randrange() function. The argument needs to be equal to the number of options, that are available
case=random.randrange(7)+1
if(case==1):
	answer="You shoud use " + get_random(tool) 
	if(random.randrange(2)):
		answer+= get_purpose() 
	answer+="."
elif(case==2):
	answer="The only way I can see this work would be" + get_purpose() + "."
elif(case==3):
	answer="Have you tried using " + get_random(tool)
	if(random.randrange(2)):
		answer+= get_purpose() 
	answer+="?"
elif(case==4):
	answer="I would just " + get_random(action)
	if(random.randrange(2)):
		answer+=get_random(target)
	answer+="."
elif(case==5):
	answer="I do not think that is possible."
	followup=False
elif(case==6):
	answer=get_random(tool).capitalize() + get_random(end)
elif(case==7):
	answer="Connect" + get_random(target) + " to" + get_random(target) + " to cause a buffer overflow and " + get_random(action) + get_random(target) + get_random(end)

## if 'followup' was not set to False, then decide wether a second sentence shall be added
if (followup and random.randrange(2)):
	case=random.randrange(5)+1
	if(case==1):
		answer+=" Maybe using " + get_random(tool)
		if(random.randrange(2)):
			answer+=" or " + get_random(tool)
		if(random.randrange(2)):
			answer+= get_purpose() 
		if(random.randrange(2)):
			answer+= " would also be a good idea" + get_random(end)
		else:
			answer+=" could also work" + get_random(end)
	elif(case==2):
		answer+=" Or just " + get_random(action) +  get_random(target) + get_random(end)
	elif(case==3):
		answer+=" Afterwards it is just a matter of trying " + get_purpose() + get_random(end)
	elif(case==4):
		answer+=" The easiest way I can think of would be"  + get_purpose() + get_random(end)
	elif(case==5):
		answer+=" Alternatively you could always "
		if(random.randrange(2)):
			answer+= get_random(action) +  get_random(target) + get_random(end)
		else:
			answer+= "try " + get_purpose() + get_random(end)

# print the final answer
print(answer)
