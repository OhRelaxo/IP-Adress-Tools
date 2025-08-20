from helper_func import generate_subnets
from tabulate import tabulate

ip = "192.168.0.0"
prefix = "28"

# kann ein String sicher als ein Integer convertiert werden? In der eingabe, also in main.py testen!

def subnet_calculator():
    ip_list = ip.split(".")
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])
    subnet = generate_subnets(ip, int(prefix), first_octet, second_octet)
    headers = ["IP-Class", "IP-Type", "Network Address", "Subnet Mask", "Inverse Mask", "Broadcast Address", "Sum Subnets",
               "Sum Hosts", "First Host", "Last Host"]

    rows = [[entry["ip-class"], entry["ip-type"], entry["network-address"], entry["subnet mask"],
             entry["inverse mask"], entry["broadcast-address"], entry["sum subnets"],
             entry["sum hosts"], entry["first host"], entry["last host"]]for entry in subnet]

    table = tabulate(rows, headers=headers, tablefmt='grid')
    print(table)

subnet_calculator()

