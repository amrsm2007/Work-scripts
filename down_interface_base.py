from jnpr.junos import Device
import time


out=open("D:\\amr_ali\python\out.txt",'w')
interfaces=open("D:\\amr_ali\python\interfaces.txt",'w')
neigh_num=open("D:\\amr_ali\python\\neigh_num.txt",'w')
devices="D:\\amr_ali\python\devices.txt"
with open(devices,'r') as f:
    devices=f.readlines()
    devices=[x.strip() for x in devices]

def match(data):
    # function to split the data to lines and retun first word on each line as list
    lines=data.splitlines()
    matched_lines = []
    interfaces=""
    for line in lines :
        line=line.split()
        if line !=[] :
            if line[0]!="Interface":
              matched_lines.append(line[0])
              interfaces+=" " + line[0]

    negibours = len(matched_lines)
    return interfaces , negibours

#words=["RST","DST","EDG","SLR","IRR","VRR","IGW","NGW","NE5"]

start_time = time.time()
for device in devices:

    with Device(host=device, user="a.abdelwahab", passwd="VGPxzbXV", port="22",gather_facts=False) as dev:

        data = dev.rpc.get_isis_adjacency_information({"format": "text"}).text
        data1,negibours=match(data)
        print(device)
        out.write(device +"  "+str(negibours)+"--->>>>>>   "+str(data1)+ "\n" )
        interfaces.write(str(data1)+"\n")
        neigh_num.write(str(negibours)+"\n")


print ( "finished in %a sec." %(time.time()-start_time))
print (" check data on following path \"D:\\amr ali\python\out.txt\"")


out.close()
interfaces.close()
neigh_num.close()