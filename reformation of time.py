class Solution:
    def maximumTime(self, time: str) -> str:
        # flag1=False/
        newTime=""
        if time[0]=="?":
            newTime+="2"
        else:
            newTime+=time[0]
        if time[1]=="?":
            flag1=True
            newTime+="9"
        else:
            newTime+=time[1]
        if int(newTime)>23 and time[1]!="?":
            newTime="1"+newTime[1:]
        elif (time[0]=="2" and time[1]=="?") or (time[0]=="?" and time[1]=="?"):
            newTime="23"


        newTime+=":"
        if time[3]=="?":
            newTime+="5"
        else:
            newTime+=time[3]
        if time[4]=="?":
            newTime+="9"
        else:
            newTime+=time[4]
        return (newTime)




