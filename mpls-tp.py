from jnpr.junos import Device
import time


start_time = time.time()

out=open("D:\\amr_ali\python\out.txt",'w')
devices="D:\\amr_ali\python\devices.txt"
ports="D:\\amr_ali\python\\ports.txt"
with open(devices,'r') as f:
    devices=f.readlines()
    devices=[x.strip() for x in devices]
with open(ports,'r') as f:
    ports=f.readlines()
    ports=[x.strip() for x in ports]

print (devices)
print (ports)
i = 0
for device in devices:

    with Device(host=device, user="a.abdelwahab", passwd="VGPxzbXV", port="22") as dev:

        data = dev.cli("show vrrp interface " + ports[i]).find()
        #data=dev.rpc.get_vrrp_interface_information(interface_name=ports[i]).text

        i+=1
        out.write(device +"    "+ ports[i-1] +"\n")
        out.write(str(len(data)))
        out.write("*"*50)

out.close()


print ( "finished in %a sec." %(time.time()-start_time))
print (" check data on following path \"D:\\amr ali\python\out.txt\"")

