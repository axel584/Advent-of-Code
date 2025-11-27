import hashlib

puzzle = 'iwrupvqb'
i = 0
while True :
    result = hashlib.md5((puzzle+str(i)).encode())
    if str(result.hexdigest())[:6]=="000000" :
        print("trouve : ",puzzle+str(i))
        exit()
    i += 1