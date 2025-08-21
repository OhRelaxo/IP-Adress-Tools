Input = "192.168.0.1"
# output: ::ffff:c0a8:1 -> c0a8 == 192.168, 1 == 0.1

def create_ipv6():
    # check if IP is correct!
    ip = list(map(lambda x: int(x), Input.split(".")))
    # make a dez to hex function, that returns a list of all the octets in hex.
    ip_hex = []
    for num in ip:
        remainder = num // 16
        # make them into hex nums
        if num % 16 == 0:
            ip_hex.append(f"{create_hex_num(remainder)}0")
        else:
            ip_hex.append(f"{create_hex_num(remainder)}{create_hex_num(num - remainder * 16)}")
    print(ip_hex)

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

create_ipv6()