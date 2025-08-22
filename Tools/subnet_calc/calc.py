import sys
from Tools.subnet_calc.helper_func import generate_subnets, ip_to_32bit
from tabulate import tabulate
import csv
import json

def subnet_calculator(ip:str, prefix:int):
    ip_list = ip.split(".")
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])
    subnet_list = generate_subnets(ip, int(prefix), first_octet, second_octet)
    return subnet_list

def create_ip_and_prefix(args):
    ip_address: str = args.subcalc
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

def create_csv(subnet_list):
    try:
        with open("subnet.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = list(subnet_list[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(subnet_list)
    except Exception as e:
        print(f"failed to create the csv, error: {e}")
        sys.exit(1)

def create_json(subnet_list):
    try:
        with open("subnet.json", mode="w", encoding="utf-8") as jsonfile:
            json.dump(subnet_list, jsonfile, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"failed to create the json file, error: {e}")
        sys.exit(1)


def output_subcalc(args):
    if args.input:
        print("error: --input is not supported by --subcalc! for help see -h or --hel")
        sys.exit(1)
    if args.verbose and not args.export:
        print("error: --verbose can only be used with --export or --input! for help see -h or --help")
        sys.exit(1) # oder return?
    ip, prefix = create_ip_and_prefix(args)
    subnet_list = subnet_calculator(ip, prefix)
    subnet_list = sorted(subnet_list, key=lambda x: ip_to_32bit(x["Network Address"]))

    if args.export:
        print(f"Data is getting exported as: {args.export}")
        if args.export == "csv":
            create_csv(subnet_list)# nur die csv erstellen
        if args.export == "json":
            create_json(subnet_list)
        if args.verbose:
            print(create_table(subnet_list))
    else:
        print(create_table(subnet_list))
    sys.exit(0)