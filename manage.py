import copy
import time

processor_nums = int(input("number of processors : "))
processors = []
for i in range(1,processor_nums+1):
    processors.append({"id":i})
    
for i in processors : 
    i["at"] = int(input("arrival time of the process {} is : ".format(i["id"])))
        
for i in processors:
    i["bt"] = int(input("brust time of process {} is : ".format(i["id"])))
    
pri=input("do you have quantum (y/n)? : ")

if pri == "y":
    quantum = int(input("your quantum : "))


print("your table : ")
for i in processors:
    print(i)
print("------------------------------")
try:
    print("your quantum : ",quantum)
    print("setup done")
except:
    print("setup done")


# calculate average waiting time and average brust time :
def avg_wt_tat(data):
    for dct in data:
        dct['tat'] = dct['ct'] - dct['at']
        dct['wt'] = dct['tat'] - dct['bt']
    tot_wt = tot_tat = 0
    for dct in data:
        tot_wt += dct['wt']
        tot_tat += dct['tat']
    ln = len(data)
    return f"average_brust_time : {int(tot_tat/ln)}, average_waiting_time : {int(tot_wt/ln)}"


# sort processes by first come first serve method :
def first_come_first_serve(data):
    arrival_time = []
    indx = 0
    for i in data:
        arrival_time.append([i['at'], i['id'], indx])
        indx += 1
    arrival_time.sort()
    curr_time = 0
    for val in arrival_time:
        if data[val[2]]['at'] > curr_time:
            curr_time += data[val[2]]['at'] - curr_time
        curr_time += data[val[2]]['bt']
        data[val[2]]['ct'] = curr_time
    return data


# sort processes by round robin method :
def round_robin(data, tq):
    rr = []
    indx = 0
    curr_time = 0
    flag = True
    for dct in data:
        rr.append([dct['at'], dct['bt'], indx])
        indx += 1
    while flag:
        for i in range(len(rr)):
            bt = rr[i][1]
            if bt != 0 and rr[i][0] < curr_time or curr_time == 0:
                if bt > tq:
                    rr[i][1] -= tq
                    curr_time += tq
                else:
                    rr[i][1] = 0
                    curr_time += bt
                    data[rr[i][2]]['ct'] = curr_time
        flg = True
        for i in rr:
            if not i[1] == 0:
                flg = False
        if flg:
            flag = False
    return data


print("1. round robin")
print("2. fcfs")
print("3. Quit\n")

while True:
    inp = int(input("submit : "))
    print("------------------------------------------\n")
        
    if inp == 1:
        processors_2 = copy.deepcopy(processors)
        sor = []
        data = round_robin(processors_2,quantum)
        data2 = avg_wt_tat(data)
        for i in processors:
            sor.append(i["id"])
        
        print("process sorted : ",sor,"\n")
        print(data2)
    
    if inp == 2:
        processors_2 = copy.deepcopy(processors)
        sor = []
        data = first_come_first_serve(processors_2)
        data2 = avg_wt_tat(data)
        for i in processors:
            sor.append(i["id"])
        
        print("process sorted : ",sor,"\n")
        print(data2)
        
    if inp == 3:
        print("Thanks for your time")
        time.sleep(3)
        
        break