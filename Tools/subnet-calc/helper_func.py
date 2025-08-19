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