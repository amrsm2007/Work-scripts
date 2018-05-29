from jnpr.junos import Device
import time


def match(data,word):
    # function to match on word on big sting and return all lines have match to the word
    lines=data.splitlines()
    matched_lines = ""
    count=0
    for line in lines :
        if word in line:
            #matched_lines += line
            #matched_lines += "\n"
            count+=1
    return matched_lines , count

start_time = time.time()

out = open("D:\\amr_ali\python\out.txt",'w')
devices = "D:\\amr_ali\python\devices.txt"
host_name = "D:\\amr_ali\python\\host_name.txt"
with open(devices,'r') as f:
    devices = f.readlines()
    devices = [x.strip() for x in devices]
with open(host_name,'r') as f:
    hosts = f.readlines()
    hosts = [x.strip() for x in hosts]

print(devices)
for device,host in zip(devices,hosts):

    with Device(host=device, user="a.abdelwahab", passwd="VGPxzbXV", port="22") as dev:


        #data = dev.cli("show route " + route + " active-path detail table Mobile_Backhaul_2G_Central | find Protocol")
        data = dev.rpc.get_log({"format": "text"},filename="messages").text
        data1,count=match(data,"IPTV")

        out.write(device +"  "+ host+"------->>>>>>   "+str(count)+ "\n" )
        #out.write("\n")
        #out.write("+"*100+"\n")
    print(host)

out.close()


print ( "finished in %a sec." %(time.time()-start_time))
print (" check data on following path \"D:\\amr ali\python\out.txt\"")
