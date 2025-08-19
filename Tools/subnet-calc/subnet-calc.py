from helper_func import calculate_octet, ip_class, ip_pub_or_pri

IP = "192.168.0.1"
Mask = "28"

# kann ein String sicher als ein Integer convertiert werden?

octet = IP.split(".")
host_bits = 32 - int(Mask)
count_host = 2 ** (host_bits - 2)
count_sub_net = 2 ** int(Mask)
first_octet = int(octet[0])
second_octet = int(octet[1])

if host_bits == 0:
    raise ValueError("the subnet mask has to be bigger than 0!")
if 1 <= host_bits <= 8:
    print(calculate_octet(host_bits))
    print(ip_class(first_octet, second_octet))
    print(ip_pub_or_pri(first_octet, second_octet))
    # den String in einer eigenen Funktion bauen, vielleicht hier einen "master string" und diesen dann in die Funktion hereingeben!
    # Nur das Vierte Octet muss berechnet werden!
    pass
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

