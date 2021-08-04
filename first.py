from netmiko import ConnectHandler

switches = ["IP_ADDRESS1", "IP_ADDRESS2", "IP_ADDRESS3", "..."]
for ip in switches:
    
    user = input("Enter username: ")
    password = input("Enter password: ")
    enablePassword = input("Enter password for enable: ")

    connectionsettings = {
        "host":ip,
        "username":user,
        "password":password,
        "device_type": "cisco_ios_telnet",
        "secret":enablePassword,
        }

    ssh = ConnectHandler(**connectionsettings)
    ssh.enable()

    command = "show clock"

    exec_cmd = ssh.send_command(command, expect_string="[DEVICENAME]")
    print(exec_cmd)

    command = "copy running-config startup-config"

    exec_cmd = ssh.send_command(command, expect_string="[DEVICENAME]")
    ssh.send_command("y", expect_string="[N]")
    print(exec_cmd)

    command = "reload"

    exec_cmd = ssh.send_command(command, expect_string="[DEVICENAME]")
    ssh.send_command("y")
    print(exec_cmd) 

    # ssh.send_command("\n")
    ssh.disconnect()

    print("\n" + ip + " is rebooting...")

print ("done")
