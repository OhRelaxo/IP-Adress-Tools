from helper_func import calculate_octet, ip_class, ip_pub_or_pri

ip = "192.168.0.1"
prefix = "28"

# kann ein String sicher als ein Integer convertiert werden?

def subnet_calculator():
    ip_list = ip.split(".")
    host_bits = 32 - int(prefix)
    count_host = 2 ** (host_bits - 2)
    count_sub_net = 2 ** int(prefix)
    first_octet = int(ip_list[0])
    second_octet = int(ip_list[1])

    if host_bits == 0:
        raise ValueError("the subnet mask has to be bigger than 0!")
    if 1 <= host_bits <= 8:
        print(calculate_octet(host_bits))
        print(ip_class(first_octet, second_octet))
        print(ip_pub_or_pri(first_octet, second_octet))
    # den String in einer eigenen Funktion bauen, vielleicht hier einen "master string" und diesen dann in die Funktion hereingeben!
    # Nur das Vierte Octet muss berechnet werden!
    elif 8 < host_bits <= 16:
    # Das Dritte und Vierte Octet muss berechnet werden!
        pass
    elif 16 < host_bits <= 24:
    # Das Zweite, Dritte und Vierte Octet muss berechnet werden!
        pass
    elif 24 < host_bits <= 31:
    # Das Erste, Zweite, Dritte und Vierte Octet muss berechnet werden!
        pass
    else:
        raise ValueError("host_bits cant be 32!")

    # Das alles noch in Sinnvolle funktionen unterteilen und die Klasse, sowie öffentlich oder privat einbauen.

    ip_list = list(map(int, ip.split(".")))
    ip_in_bit = 0
    shift = 24
    for octet in ip_list:
        ip_in_bit += octet << shift
        shift -= 8
    print(bin(ip_in_bit))
    mask = (0xFFFFFFFF << (32 - int(prefix)) & 0xFFFFFFFF)
    network_adr = ip_in_bit & mask
    inverse_mask = mask ^ 0xFFFFFFFF
    broadcast = ip_in_bit | inverse_mask
    print(bin(broadcast))
    if int(prefix) > 31:
        return # kann kein subnetz mit einem Prefix berechnen welcher größer als 31 ist :(
    hosts = 2 ** (32 - int(prefix)) - 2
    if hosts >= 1:
        first_host = network_adr + 1
        last_host = network_adr + hosts
    else:
        first_host = "-"
        last_host = "-"
    #192.168.0.1
    print(f"{first_host >> 24 & 0xFF}.{first_host >> 16 & 0xFF}.{first_host >> 8 & 0xFF}.{first_host >> 0 & 0xFF}")
    # 11000000101010000000000000000001 >> 24 -> 11000000
    # 11000000101010000000000000000001 >> 16 -> 10101000
    # 11000000101010000000000000000001 >> 8 -> 0
    # 11000000101010000000000000000001 >> 0 -> 1


subnet_calculator()
