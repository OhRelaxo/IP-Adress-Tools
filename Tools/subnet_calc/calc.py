from Tools.subnet_calc.helper_func import generate_subnets
from tabulate import tabulate

def subnet_calculator(ip:str, prefix:int):
    ip_list = ip.split(".")
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])
    subnet_list = generate_subnets(ip, int(prefix), first_octet, second_octet)
    headers = ["IP-Class", "IP-Type", "Network Address", "Subnet Mask", "Inverse Mask", "Broadcast Address", "Sum Subnets",
               "Sum Hosts", "First Host", "Last Host"]

    rows = [subnet.values() for subnet in subnet_list]
    # maybe make the output a bit smaller if possible?
    table = tabulate(rows, headers=headers, tablefmt='grid')
    return table

# I could rebase this but why should I, it works :)
def exec_subcalc(args):
    ip_address: str = args.subcalc
    if "/" not in ip_address:
        print("please use a / to indicate the prefix, for help see -h or --help")
        return
    prefix = ip_address.split("/", 1)
    ip = prefix[0]

    if prefix[1].isdigit():
        prefix = int(prefix[1])
    else:
        print("please use a number as the prefix, for help see -h or --help")
        return
    if prefix > 32:
        print("The prefix cant be bigger than 32, that is just not possible with 4 Bytes sorry :(, for help see -h or --help")
        return

    print(subnet_calculator(ip, prefix))

