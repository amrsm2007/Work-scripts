from ncclient import manager

#x=manager.connect(host="10.142.43.50",username="a.abdelwahab",password="VGPxzbXV",port=22,hostkey_verify=False,device_params={'name':'iosxe'})
with manager.connect_ssh(host="10.216.45.114", port=23, username="a.abdelwahab",
                         password="VGPxzbXV", hostkey_verify=False,
                         device_params={'name':'iosxe','local': False},
                         allow_agent=False, look_for_keys=False) as m:

                    m.execute("show interfaces description")
