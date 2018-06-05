from jnpr.junos import Device
import time


out=open("D:\\amr_ali\python\out.txt",'w')
devices="D:\\amr_ali\python\devices.txt"
with open(devices,'r') as f:
    devices=f.readlines()
    devices=[x.strip() for x in devices]

def match(data,words):
    # function to match on word on big sting and return all lines have match to the word
    lines=data.splitlines()
    matched_lines = []
    count=0
    negibours=len(lines)
    for line in lines :
        for word in words:
            if word in line:
                line=line.split()
                matched_lines.append(line[0])
                count += 1
    return matched_lines , negibours

words=["RST","DST","EDG","SLR","IRR","VRR","IGW","NGW","NE5"]

start_time = time.time()
for device in devices:

    with Device(host=device, user="a.abdelwahab", passwd="VGPxzbXV", port="22",gather_facts=False) as dev:


        #data = dev.cli("show route " + route + " active-path detail table Mobile_Backhaul_2G_Central | find Protocol")
        data = dev.rpc.get_isis_adjacency_information({"format": "text"}).text
        data1,negibours=match(data,words)

        out.write(device +"  "+str(negibours)+"------->>>>>>   "+str(data1)+ "\n" )

print ( "finished in %a sec." %(time.time()-start_time))
print (" check data on following path \"D:\\amr ali\python\out.txt\"")


out.close()