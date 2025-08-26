import sys
from Tools.subnet_calc.helper_func import generate_subnets, ip_to_32bit
from tabulate import tabulate
from Tools.input_export import export_csv, export_json

def subnet_calculator(ip:str, prefix:int):
    ip_list = ip.split(".")
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])
    subnet_list = generate_subnets(ip, int(prefix), first_octet, second_octet)
    return subnet_list

def create_ip_and_prefix(args):
    ip_address: str = args.subnet
    if "/" not in ip_address:
        print("please use a / to indicate the prefix, for help see -h or --help")
        sys.exit(1)
    prefix = ip_address.split("/", 1)
    ip = prefix[0]

    if prefix[1].isdigit():
        prefix = int(prefix[1])
    else:
        print("please use a number as the prefix, for help see -h or --help")
        sys.exit(1)
    if prefix > 32:
        print(
            "The prefix cant be bigger than 32, that is just not possible with 4 Bytes sorry :(, for help see -h or --help")
        sys.exit(1)
    return ip, prefix

def create_table(subnet_list):
    headers = subnet_list[0].keys()
    rows = [subnet.values() for subnet in subnet_list]
    # maybe make the output a bit smaller if possible?
    table = tabulate(rows, headers=headers, tablefmt='grid')
    return table

def output_subnet(args):
    if args.input_file:
        print("error: --input-file is not supported by --subnet! for help see -h or --help")
        sys.exit(1)
    if args.verbose and not args.output_format:
        print("error: --verbose can only be used with --output-format or --input-file! for help see -h or --help")
        sys.exit(1)
    ip, prefix = create_ip_and_prefix(args)
    subnet_list = subnet_calculator(ip, prefix)
    subnet_list = sorted(subnet_list, key=lambda x: ip_to_32bit(x["Network Address"]))

    if args.output_format:
        print(f"Data is getting exported as: {args.output_format}")
        if args.output_format == "csv":
            export_csv(subnet_list, "subnet.csv", list(subnet_list[0].keys()))
        if args.output_format == "json":
            export_json(subnet_list, "subnet.json")
        if args.verbose:
            print(create_table(subnet_list))
    else:
        print(create_table(subnet_list))
    sys.exit(0)