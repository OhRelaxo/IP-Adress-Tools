def ip_to_32bit(ip: str) -> int:
    octets = list(map(int, ip.split(".")))
    # basic validation (optional but safe)
    if len(octets) != 4 or any(o < 0 or o > 255 for o in octets):
        raise ValueError("invalid IPv4 address")
    return sum(octet << (8 * (3 - i)) for i, octet in enumerate(octets))

def ip_class(first_octet: int, second_octet: int) -> str:
    if 0 < first_octet <= 126:
        return "A"
    elif first_octet == 127:
        return "Loopback"
    elif first_octet == 169 and second_octet == 254:
        return "Link-local (APIPA)"
    elif 128 <= first_octet <=  191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    elif 224 <= first_octet <= 239:
        print("you should not use class D or E for subnetting!")
        return "D"
    elif 240 <= first_octet <= 255:
        print("you should not use class D or E for subnetting!")
        return "E"
    else:
        raise ValueError("the first octet is bigger than 255 :(")

def ip_pub_or_pri(first_octet: int, second_octet: int) -> str:
    if first_octet == 10:
        return "private"
    elif first_octet == 172 and 16 <= second_octet <= 31:
        return "private"
    elif first_octet == 192 and second_octet == 168:
        return "private"
    else:
        return "public"

def fancy_string(bit32_component: int) -> str:
    return f"{bit32_component >> 24 & 0xFF}.{bit32_component >> 16 & 0xFF}.{bit32_component >> 8 & 0xFF}.{bit32_component >> 0 & 0xFF}"

def subnet_count(ip_cl: str, new_prefix: int) -> int:
    default_prefix = {"A": 8, "B": 16, "C": 24}.get(ip_cl, 24)
    if new_prefix >= default_prefix:
        return 2 ** (new_prefix - default_prefix)
    return 1

def calc_hosts(prefix: int) -> int:
    if prefix >= 31:
        return 0
    return 2 ** (32 - prefix) - 2


def generate_subnets(ip: str, prefix: int, first_octet: int, second_octet: int):
    subnet_data = []
    ip_cl = ip_class(first_octet, second_octet)
    ip_type = ip_pub_or_pri(first_octet, second_octet)
    hosts = calc_hosts(prefix)

    subnet_size = 2 ** (32 - prefix)
    subnet_mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF

    # Start from the network address of the given IP
    ip_as_int = ip_to_32bit(ip) & subnet_mask
    count = subnet_count(ip_cl, prefix)

    for _ in range(count):
        network_adr = ip_as_int
        broadcast = network_adr + subnet_size - 1
        inverse_mask = subnet_mask ^ 0xFFFFFFFF

        if hosts >= 1:
            first_host = fancy_string(network_adr + 1)
            last_host = fancy_string(broadcast - 1)
        else:
            first_host = "-"
            last_host = "-"

        subnet = {
            "IP-Class": ip_cl,
            "IP-Type": ip_type,
            "Network Address": fancy_string(network_adr),
            "Subnet Mask": fancy_string(subnet_mask),
            "Inverse Mask": fancy_string(inverse_mask),
            "Broadcast Address": fancy_string(broadcast),
            "Sum Subnets": count,
            "Sum Hosts": hosts,
            "First Host": first_host,
            "Last Host": last_host
        }
        subnet_data.append(subnet)
        ip_as_int += subnet_size

    return subnet_data