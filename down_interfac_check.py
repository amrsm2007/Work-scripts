from jnpr.junos import Device
import time

import win32com.client as win32





out=open("D:\\amr_ali\python\out.txt",'w')
interfaces="D:\\amr_ali\python\interfaces.txt"
neigh_num="D:\\amr_ali\python\\neigh_num.txt"
devices="D:\\amr_ali\python\devices.txt"
host_name = "D:\\amr_ali\python\\host_name.txt"
with open(devices,'r') as f:
    devices=f.readlines()
    devices=[x.strip() for x in devices]

with open(interfaces,'r') as f:

    interfaces= f.readlines()
    interfaces=[x.strip().split() for x in interfaces]

with open(neigh_num,'r') as f:
    neigh_num=f.readlines()
    neigh_num=[x.strip() for x in neigh_num]


with open(host_name,'r') as f:
    hosts = f.readlines()
    hosts = [x.strip() for x in hosts]


def match(data):
    # function to split the data to lines and retun first word on each line as list
    lines=data.splitlines()
    matched_lines = []
    for line in lines :
        line=line.split()
        if line !=[] :
            matched_lines.append(line[0])

    negibours = len(matched_lines)-1
    return matched_lines[1:] , negibours
def check_interfaces(I1,I2,n1,n2):
    is_interface_down=True
    down = []
    if int(n1) == int(n2):
        is_interface_down=False
    else:

        for x in I1:
            if x not in I2:
                down.append(x)
    return is_interface_down,down





#words=["RST","DST","EDG","SLR","IRR","VRR","IGW","NGW","NE5"]

start_time = time.time()

while True :
    start_time = time.time()
    print (time.ctime())
    for device,host,I1,n1 in zip(devices,hosts,interfaces,neigh_num):

      with Device(host=device, user="a.abdelwahab", passwd="VGPxzbXV", port="22",gather_facts=False) as dev:

        data = dev.rpc.get_isis_adjacency_information({"format": "text"}).text
        I2,n2=match(data)
        is_down,down=check_interfaces(I1,I2,n1,n2)
        print (int(n1) != int(n2) ,device,n1,n2)
        print(down)
        if is_down :
            down_interfaces=""
            for interface in down:

                desc=dev.rpc.get_interface_information({"format": "text"},descriptions=True,interface_name=interface).text
                down_interfaces += host +"   "+ str(desc)+"\n"

                out.write(host +"   "+ str(desc)+"\n")

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = 'a.abdelwahab@mobily.com.sa';'f.desai@mobily.com.sa'
            mail.Subject = 'DOWN INTERFACES on '+host
            mail.Body = down_interfaces
            # mail.HTMLBody = '<h2>kindly check down interface in attached</h2>'

            # attachment  = "D:\\amr_ali\python\out.txt"
            # mail.Attachments.Add(attachment)
            mail.Send()
    print("finished in %a sec." % (time.time() - start_time))
    time.sleep(60*6)



#print (" check data on following path \"D:\\amr ali\python\out.txt\"")


out.close()