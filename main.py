IP = "192.168.0.1"
Mask = "28"

IP_list = IP.split(".")

host_bits = 32 - int(Mask)
# wenn die host bits größer als 8 sind, müssen wir auch das Dritte Octet berechnen

host_range = 2 ** host_bits

host_ips = host_range - 2

# wir kenn das Octet -> mit switch case herausfinden z.B. im Virten ist alles was >= 24 ist

octet_list = []
# [{network: 0, start_host: 1, end_host: 14, broadcast: 15}]
end_host = host_range - 2
broadcast = host_range - 1

for i in range(0, int(256 / host_range)):
    network = i * host_range
    start_host = 1 + network
    current_subnet = {"network" : network, "start_host": 1 + network,
                      "end_host": end_host + network, "broadcast": broadcast + network}
    octet_list.append(current_subnet)

# für jedes Octet welches wir benötigen und können wir einfach den ganzen Spaß zusammen rechnen
print(octet_list)

