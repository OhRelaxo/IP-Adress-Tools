def calculate_32_bit_ip(ip:str) -> int:
    ip_list = list(map(int, ip.split(".")))
    ip_in_bit = 0
    shift = 24
    for octet in ip_list:
        ip_in_bit += octet << shift
        shift -= 8
    print(bin(ip_in_bit))
    return ip_in_bit

def ip_class(first_octet: int, second_octet: int) -> str:
    if 0 <= first_octet <= 126:
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
        return "D"
    elif 240 <= first_octet <= 255:
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

def build_subnet(ip: str, prefix: int, first_octet: int, second_octet: int):
    ip_in_bit = calculate_32_bit_ip(ip)
    subnet_mask = (0xFFFFFFFF << (32 - prefix) & 0xFFFFFFFF)
    network_adr = ip_in_bit & subnet_mask
    inverse_mask = subnet_mask ^ 0xFFFFFFFF
    broadcast = ip_in_bit | inverse_mask
    ip_cl = ip_class(first_octet, second_octet)
    ip_type = ip_pub_or_pri(first_octet, second_octet)
    if prefix > 31:
        hosts = 0 # kann kein subnetz mit einem Prefix berechnen welcher größer als 31 ist :(
    else: hosts = 2 ** (32 - prefix) - 2
    if hosts >= 1:
        first_host = fancy_string(network_adr + 1)
        last_host = fancy_string(network_adr + hosts)
    else:
        first_host = "-"
        last_host = "-"

    subnet = {
        "ip-class": ip_cl,
        "ip-type": ip_type,
        "network-address": fancy_string(network_adr),
        "subnet mask": fancy_string(subnet_mask),
        "inverse mask": fancy_string(inverse_mask),
        "broadcast-address": fancy_string(broadcast),
        "sum subnets": 2 ** prefix,
        "sum hosts": hosts,
        "first host": first_host,
        "last host": last_host
    }
    return subnet