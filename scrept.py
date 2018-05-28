from jnpr.junos import Device
import time


start_time = time.time()

out=open("D:\\amr_ali\python\out.txt",'w')
devices="D:\\amr_ali\python\devices.txt"
routes="D:\\amr_ali\python\\routes.txt"
with open(routes,'r') as f:
    routes=f.readlines()
    routes=[x.strip() for x in routes]

print (routes)

with Device(host="10.212.0.26", user="a.abdelwahab", passwd="VGPxzbXV", port="22") as dev:
    for route in routes :
        data = dev.cli("show route " + route + " active-path detail table Mobile_Backhaul_2G_Central | find Protocol")
        i = data.find("Protocol")
        j = data.find("\n",i)

       # data1=dev.rpc.get_route_information(destination=route, detail=True, table='Mobile_Backhaul_2G_Central', active_path=True )

        out.write(data[i:j] + "   ->->"+ route)
        out.write("\n")




out.close()


print ( "finished in %a sec." %(time.time()-start_time))
print (" check data on following path \"D:\\amr ali\python\out.txt\"")

