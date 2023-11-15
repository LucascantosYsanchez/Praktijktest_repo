print("Connecting via SSH => show interface status (brief)")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="sandbox-iosxe-recomm-1.cisco.com",
    port="22",
    username="developer",
    password="lastorangerestoreball8876"
    )
output=sshCli.send_command("show ip interface brief")
print(output)
