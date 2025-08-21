import sys
# 192.168.0.1: output: 0000:0000:0000:0000:0000:ffff:c0a8:0001 -> c0a8 == 192.168, 0001 == 0.1

def create_ipv6(args):
    ipv4_hex = convert_ipv4_to_hex(args.ip4to6)
    ipv6 = f"0000:0000:0000:0000:0000:ffff:{"".join(ipv4_hex[:2])}:{"".join(ipv4_hex[2:])}"
    print(ipv6)
    sys.exit(0)
    # add the rest of the ipv6

def convert_ipv4_to_hex(input):
    ip = split_ipv4(input)
    ip_hex = []

    for num in ip:
        remainder = num // 16
        if num % 16 == 0:
            ip_hex.append(f"{create_hex_num(remainder)}0")
        else:
            ip_hex.append(f"{create_hex_num(remainder)}{create_hex_num(num - remainder * 16)}")
    return ip_hex

def split_ipv4(input):
    ip = list(map(int, input.split(".")))
    if len(ip) != 4 or any(o < 0 or o > 255 for o in ip):
        print("invalid IPv4 address")
        sys.exit(1)
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