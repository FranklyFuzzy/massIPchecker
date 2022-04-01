import re  #regex needed to find IPs   #http://searchsignals.com/tutorials/reverse-dns-lookup/
import socket #socket needed to evaluate reverse IP lookup
nhand=input('File name please: ')
try:
    fhand=open(nhand)
except:
    print("File" ,nhand, "cannot be opened")
    quit()

mylist=list()
fhand=open(nhand)
for x in fhand:
    x=x.rstrip()
    pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    finalIP = re.findall(pattern, x)
    if len(finalIP) < 1: continue
    mylist.append(finalIP[0]) #calling sub 0 makes sure we arnt nesting lists

print()
count=0
for line in mylist:
    count += 1
print('I have found', count, 'total IPs')

print()
print('IP : Count')
mylist2=list()
potato=dict()
for namez in mylist:
    potato[namez] = potato.get(namez, 0) + 1
for key in potato:
    # print(key, ":", potato[key])
    mylist2.append(key)

tmp=list()
for k, v in potato.items():
    tmp.append((v,k))
tmp = sorted(tmp, reverse=True)
for v,k in tmp:
    print(k,":", v)  #pretty print

xount = 0
for line in tmp:
    xount +=1
print()
print('Counted', xount, 'unique IPs')

print()
for x in mylist2:
    try:
        reversed_dns = socket.gethostbyaddr(x)
    except:
        print('Could not retreive reverse IP lookup',x)
        continue
    else:
        print(x, ':', reversed_dns[0])
print()
