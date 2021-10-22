command="(al)G(al)()()G"
string=""
i=0
while(i<len(command)):
    if command[i]=="G":
        string+=command[i]
    elif command[i]=="(" and command[i+1]=="a" and command[i+2]=="l":
        string+="al"
        i+=3
    elif command[i]=="(" and command[i+1]==")":
        string+="o"
        i+=1
    i+=1


print(string)
