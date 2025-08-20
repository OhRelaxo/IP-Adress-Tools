from helper_func import build_subnet

ip = "192.168.0.1"
prefix = "28"

# kann ein String sicher als ein Integer convertiert werden?

def subnet_calculator():
    ip_list = ip.split(".")
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])
    subnet = build_subnet(ip, int(prefix), first_octet, second_octet)
    print(subnet)

subnet_calculator()
