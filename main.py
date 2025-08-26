from Tools.shorten_lengthen_ipv6.output import output_shorten_ipv6, output_lenghten_ipv6
from Tools.subnet_calc.calc import output_subnet
from Tools.ip_conversion.convert_ipv4 import output_convert_ipv4
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--subnet", type=str, help="Calculate the subnet of a given IP address")
    parser.add_argument("-o", "--output-format", choices=["csv", "json"], help="Export format")
    parser.add_argument("-i", "--input-file", type=str, help="CSV input file")
    parser.add_argument("-c", "--convert-ipv4", nargs="?", help="Convert an IPv4 address to IPv6")
    parser.add_argument("--shorten-ipv6", nargs="?", help="Shorten a full IPv6 address")
    parser.add_argument("--expand-ipv6", nargs="?", help="Expand a shortened IPv6 address")
    parser.add_argument("--full-ipv6", action="store_true", help="Output full (non-shortened) IPv6 address, can only be used with convert-ipv4")
    parser.add_argument("-v", "--verbose", action="store_true", help="Also output data to the console")

    args = parser.parse_args()

    if args.subnet:
        output_subnet(args)

    if args.convert_ipv4:
        output_convert_ipv4(args)

    if args.shorten_ipv6:
        output_shorten_ipv6(args)

    if args.expand_ipv6:
        output_lenghten_ipv6(args)

if __name__ == '__main__':
    main()