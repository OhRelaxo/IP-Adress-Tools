def create_long_ipv6(ip_adr):
    long_ipv6 = []
    for adr in ip_adr:
        current_ip = adr.split("::")
        if len(current_ip) != 2:
            print("error: invalid ipv6!")
            continue

        new_ipv6 = current_ip[0].split(":")
        second_half = current_ip[1].split(":")
        count_octet = len(new_ipv6) + len(second_half)
        while count_octet < 8:
            new_ipv6.append("")
            count_octet += 1
        new_ipv6.extend(second_half)

        for i in range(len(new_ipv6)):
            octet = new_ipv6[i]
            while len(octet) < 4:
                octet = "0" + octet
            new_ipv6[i] = octet
        long_ipv6.append({"IPv6":":".join(new_ipv6)})
    return long_ipv6