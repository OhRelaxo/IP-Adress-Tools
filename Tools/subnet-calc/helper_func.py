def calculate_octet(host_bits):
    host_range = 2 ** host_bits
    octet_list = []
    end_host = host_range - 2
    broadcast = host_range - 1
    for i in range(0, int(256 / host_range)):
        network = i * host_range
        current_subnet = {"network" : network, "start_host": 1 + network,
                          "end_host": end_host + network, "broadcast": broadcast + network}
        octet_list.append(current_subnet)
    return octet_list

def ip_class(first_octet, second_octet):
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

def ip_pub_or_pri(first_octet, second_octet):
    if first_octet == 10:
        return "private"
    elif first_octet == 172 and 16 <= second_octet <= 31:
        return "private"
    elif first_octet == 192 and second_octet == 168:
        return "private"
    else:
        return "public"