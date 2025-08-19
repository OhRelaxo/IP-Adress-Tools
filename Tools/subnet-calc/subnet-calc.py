from helper_func import calculate_octet

IP = "192.168.0.1"
Mask = "28"

octet = IP.split(".")
host_bits = 32 - int(Mask)

# um die Klasse und vlt. den typ (also öffentlich oder privat) alles in Bit umwandeln und dann vergleichen?

if host_bits == 0:
    raise ValueError("the subnet mask has to be bigger than 0!")
if 1 <= host_bits <= 8:
    print(calculate_octet(host_bits))
    # Nur das Vierte Octet muss berechnet werden!
    pass
elif 8 > host_bits <= 16:
    # Das Dritte und Vierte Octet muss berechnet werden!
    pass
elif 16 > host_bits <= 24:
    # Das Zweite, Dritte und Vierte Octet muss berechnet werden!
    pass
elif 24 > host_bits <= 31:
    # Das Erste, Zweite, Dritte und Vierte Octet muss berechnet werden!
    pass
else:
    raise ValueError("host_bits cant be 32!")

