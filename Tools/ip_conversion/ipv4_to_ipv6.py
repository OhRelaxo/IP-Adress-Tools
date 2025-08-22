import sys
import os
import csv
# 192.168.0.1: output: 0000:0000:0000:0000:0000:ffff:c0a8:0001 -> c0a8 == 192.168, 0001 == 0.1

def create_ipv6(ip_adr):
    ipv6_adr = []
    for ip in ip_adr:
        ipv4_hex = convert_ipv4_to_hex(ip)
        if not ipv4_hex:
            continue
        ipv6 = f"0000:0000:0000:0000:0000:ffff:{"".join(ipv4_hex[:2])}:{"".join(ipv4_hex[2:])}"
        ipv6_adr.append(ipv6)
    if not ipv6_adr:
        print("fatal error: no IPv6 address was generated!")
        sys.exit(1)
    return ipv6_adr
    # add the rest of the ipv6

def convert_ipv4_to_hex(ip_str):
    ip = split_ipv4(ip_str)
    if not ip:
        return None
    ip_hex = []

    for num in ip:
        remainder = num // 16
        if num % 16 == 0:
            ip_hex.append(f"{create_hex_num(remainder)}0")
        else:
            ip_hex.append(f"{create_hex_num(remainder)}{create_hex_num(num - remainder * 16)}")
    return ip_hex

def split_ipv4(ip_str):
    ip = list(map(int, ip_str.split(".")))
    if len(ip) != 4 or any(o < 0 or o > 255 for o in ip):
        print("error: invalid IPv4 address")
    return ip

def create_hex_num(num):
    match num:
        case 10:
            return "a"
        case 11:
            return "b"
        case 12:
            return "c"
        case 13:
            return "d"
        case 14:
            return "e"
        case 15:
            return "f"
        case _:
            return num

def input_csv(args):
    ip_adr = []
    working_dir = os.getcwd()
    file_path = os.path.join(working_dir, args.input)
    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    ip_adr.append(row)
                continue
    except Exception as e:
        print(f"error: failed to read csv file: {e}")
        sys.exit(1)

    return ip_adr

def export_csv(ipv6_adr):
    try:
        with open("ip4to6.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = "IPv6"
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(ipv6_adr)
    except Exception as e:
        print(f"failed to create the csv, error: {e}")
        sys.exit(1)

def output_ip4to6(args):
    if args.export:
        print("error: --export is not support with ip4to6 for help see -h or --hel")
        sys.exit(1)
    if args.verbose and not args.input:
        print("error: you can only use verbose with the --export or the --input flag! for help see -h or --hel")
        sys.exit(1)

    if args.input:
        print("converting...")
        ipv6_adr = create_ipv6(input_csv(args))
        export_csv(ipv6_adr)
        if args.verbose:
            for ipv6 in ipv6_adr:
                print(ipv6)

    else:
        ip_adr = [args.ip4to6]
        print(create_ipv6(ip_adr)[0])