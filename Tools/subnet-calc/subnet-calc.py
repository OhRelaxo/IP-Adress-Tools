from helper_func import generate_subnets

ip = "192.168.0.0"
prefix = "28"

# kann ein String sicher als ein Integer convertiert werden? In der eingabe, also in main.py testen!

def subnet_calculator():
    ip_list = ip.split(".")
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])
    subnet = generate_subnets(ip, int(prefix), first_octet, second_octet)
    print(subnet)


subnet_calculator()

