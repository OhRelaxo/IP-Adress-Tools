import sys
from Tools.input_output import input_csv, export_csv

def create_ipv6(ip_adr, toggle):
    ipv6_adr = []
    for ip in ip_adr:
        ipv4_hex = convert_ipv4_to_hex(ip)
        if not ipv4_hex:
            continue
        if toggle:
            ipv6 = f"0000:0000:0000:0000:0000:ffff:{"".join(ipv4_hex[:2])}:{"".join(ipv4_hex[2:])}"
        else:
            ipv4_joined = shorten(ipv4_hex)
            ipv6 = f"::ffff:{ipv4_joined[0]}:{ipv4_joined[1]}"
        ipv6_adr.append({"IPv6":ipv6})
    if not ipv6_adr:
        print("fatal error: no IPv6 address was generated!")
        sys.exit(1)
    return ipv6_adr

def shorten(ipv4_hex):
    joined = ["".join(ipv4_hex[:2]), "".join(ipv4_hex[2:])]
    for i in range(0, len(joined)):
        ipv6 = joined[i]
        if ipv6.startswith("0") and len(ipv6) > 1:
            ipv6 = ipv6.lstrip("0")
            if not ipv6:
                ipv6 = "0"
            joined[i] = ipv6
    return joined

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

def output_ip4to6(args):
    if args.export:
        print("error: --export is not support with ip4to6 for help see -h or --hel")
        sys.exit(1)
    if args.verbose and not args.input:
        print("error: you can only use verbose with the --export or the --input flag! for help see -h or --hel")
        sys.exit(1)

    if args.input:
        print("converting...")
        ipv6_list = create_ipv6(input_csv(args), args.long)
        export_csv(ipv6_list, "ip4to6.csv", ["IPv6"])
        if args.verbose:
            # make this look better!
            for ipv6 in ipv6_list:
                print(ipv6)

    else:
        ip_adr = [args.ip4to6]
        # make this look better!
        print(create_ipv6(ip_adr, args.long)[0])