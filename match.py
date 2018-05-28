from jnpr.junos import Device
import time


def match(data,word):
    # function to match on word on big sting and return all lines have match to the word
    lines=data.splitlines()
    matched_lines = ""
    for line in lines :
        if word in line:
            matched_lines += line
            matched_lines += "\n"
    return out

start_time = time.time()

out = open("D:\\amr_ali\python\out.txt",'w')
devices = "D:\\amr_ali\python\devices.txt"
routes = "D:\\amr_ali\python\\routes.txt"
with open(routes,'r') as f:
    routes = f.readlines()
    routes = [x.strip() for x in routes]

print(routes)

with Device(host="10.212.0.26", user="a.abdelwahab", passwd="VGPxzbXV", port="22") as dev:
    for route in routes :
        #data = dev.cli("show route " + route + " active-path detail table Mobile_Backhaul_2G_Central | find Protocol")
        data = dev.rpc.get_route_information({"format": "text"}, destination=route, detail=True,
                                              table='Mobile_Backhaul_2G_Central', active_path=True).text
        data1=match(data,"Protocol")

        out.write(route + "   ->->"+ data1 )
        out.write("\n")

out.close()


print ( "finished in %a sec." %(time.time()-start_time))
print (" check data on following path \"D:\\amr ali\python\out.txt\"")

