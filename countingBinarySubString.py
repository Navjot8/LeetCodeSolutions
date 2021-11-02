s = "00011100"
if s[0] == "0":
    nextOne=s.find("1")
    temp0=s[:nextOne]
    print("Temp0 is ",temp0)
    tempString=s[nextOne:]
    nextZero=tempString[nextOne:].find("0")
    temp1=tempString[:nextZero]
    print("temp1 is ",temp1)
    # if len(temp0)
