
def create_shorten_ipv6(data):
    ip_adr = []
    for adr in data:
        ipv6_octets = adr.split(":")
        ipv6 = shorten_ipv6(ipv6_octets)
        zero_blocks = calc_zero_blocks(ipv6)

        if not zero_blocks:
            continue

        if len(zero_blocks) == 1:
            ip_adr.append({"IPv6":one_zero_block(zero_blocks, ipv6)})
        else:
            ip_adr.append({"IPv6":more_than_one_zero_block(zero_blocks, ipv6)})
    return ip_adr

def shorten_ipv6(ipv6_octets):
    for i in range(0, len(ipv6_octets)):
        ipv6 = ipv6_octets[i]
        if ipv6.startswith("0") and len(ipv6) > 1:
            ipv6 = ipv6.lstrip("0")
            if not ipv6:
                ipv6 = "0"
            ipv6_octets[i] = ipv6
    return ipv6_octets


def calc_zero_blocks(ipv6):
    zero_blocks = []
    block = []
    for i in range(0, len(ipv6)):
        octet = ipv6[i]
        if octet.startswith("0") and len(octet) == 1:
            block.append(i)
        else:
            if len(block) > 1:
                zero_blocks.append(block)
            block = []

    if len(block) > 1:
        zero_blocks.append(block)

    return zero_blocks

def one_zero_block(zero_blocks, ipv6):
    largest_num = max(zero_blocks[0])
    smallest_num = min(zero_blocks[0])
    if smallest_num == 0:
        ipv6[smallest_num] = ""
        smallest_num += 1
    ipv6[largest_num] = ""
    del ipv6[smallest_num: largest_num]
    ipv6 = ":".join(ipv6)
    return ipv6

def more_than_one_zero_block(zero_blocks, ipv6):
    biggest_block = []
    for block in zero_blocks:
        if len(block) > len(biggest_block):
            biggest_block = block
    largest_num = max(biggest_block)
    smallest_num = min(biggest_block)
    if smallest_num == 0:
        ipv6[smallest_num] = ""
        smallest_num += 1
    ipv6[largest_num] = ""
    del ipv6[smallest_num: largest_num]
    ipv6 = ":".join(ipv6)
    return ipv6