import sys

put = "ffff:ffff:0000:0000:0000:c0a8:0000:0000"

def shorten():
    ipv6 = put.split(":")
    for i in range(0, len(ipv6)):
        octet = ipv6[i]
        if octet.startswith("0") and len(octet) > 1:
            octet = octet.lstrip("0")
            if not octet:
                octet = "0"
            ipv6[i] = octet

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

    if not zero_blocks:
        print(ipv6)
        sys.exit(0)

    if len(zero_blocks) == 1:
        largest_num = max(zero_blocks[0])
        smallest_num = min(zero_blocks[0])
        ipv6[largest_num] = ""
        del ipv6[smallest_num: largest_num]
        ipv6 = ":".join(ipv6)
        print(ipv6)
        sys.exit(0)

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
    print(ipv6)
    sys.exit(0)

shorten()