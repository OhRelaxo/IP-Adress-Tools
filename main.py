from Tools.shorten_lengthen_ipv6.output import output_shorten_ipv6, output_lenghten_ipv6
from Tools.subnet_calc.calc import output_subnet
from Tools.ip_conversion.convert_ipv4 import output_convert_ipv4
import argparse

def main():
    subnet_parser = argparse.ArgumentParser(prog="subnet")
    subnet_parser.add_argument("-s", "--subnet", type=str, help="Calculate the subnet of a given IP address")
    subnet_parser.add_argument("-o", "--output-format", choices=["csv", "json"], help="Export format")
    subnet_parser.add_argument("-v", "--verbose", action="store_true", help="Also output data to the console")

    convert_ipv4_parser = argparse.ArgumentParser(prog="convert")
    convert_ipv4_parser.add_argument("-c", "--convert-ipv4", nargs="?", help="Convert an IPv4 address to IPv6")
    convert_ipv4_parser.add_argument("--full-ipv6", action="store_true", help="Output full (non-shortened) IPv6 address, can only be used with convert-ipv4")
    convert_ipv4_parser.add_argument("-i", "--input-file", type=str, help="CSV input file")
    convert_ipv4_parser.add_argument("-v", "--verbose", action="store_true", help="Also output data to the console")

    shorten_ipv6_parser = argparse.ArgumentParser(prog="shorten")
    shorten_ipv6_parser.add_argument("--shorten-ipv6", nargs="?", help="Shorten a full IPv6 address")
    shorten_ipv6_parser.add_argument("-i", "--input-file", type=str, help="CSV input file")
    shorten_ipv6_parser.add_argument("-v", "--verbose", action="store_true", help="Also output data to the console")

    expand_ipv6_parser = argparse.ArgumentParser(prog="expand")
    expand_ipv6_parser.add_argument("--expand-ipv6", nargs="?", help="Expand a shortened IPv6 address")
    expand_ipv6_parser.add_argument("-i", "--input-file", type=str, help="CSV input file")
    expand_ipv6_parser.add_argument("-v", "--verbose", action="store_true", help="Also output data to the console")

    tools_parser = argparse.ArgumentParser(prog="IP-Address-Tools", parents=[subnet_parser, convert_ipv4_parser, shorten_ipv6_parser, expand_ipv6_parser], conflict_handler='resolve')

    tools_args = tools_parser.parse_args()

    if tools_args.subnet:
        output_subnet(tools_args)

    if tools_args.convert_ipv4:
        output_convert_ipv4(tools_args)

    if tools_args.shorten_ipv6:
        output_shorten_ipv6(tools_args)

    if tools_args.expand_ipv6:
        output_lenghten_ipv6(tools_args)

if __name__ == '__main__':
    main()