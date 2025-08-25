import sys

from Tools.input_export import input_csv, export_csv
from Tools.shorten_lengthen_ipv6.shorten import create_shorten_ipv6


def output_shorten_ipv6(args):
    if args.export:
        print("error: --export is not support with shortenipv6 for help see -h or --help")
        sys.exit(1)
    if args.verbose and not args.input:
        print("error: you can only use verbose with the --export or the --input flag! for help see -h or --help")
        sys.exit(1)

    if args.input:
        print("converting...")
        ipv6_list = create_shorten_ipv6(input_csv(args))
        export_csv(ipv6_list, "shortenipv6.csv", ["IPv6"])
        if args.verbose:
            for ipv6 in ipv6_list:
                print(ipv6["IPv6"])
    else:
        ip_adr = [args.shortenipv6]
        shorten_ipv6 = create_shorten_ipv6(ip_adr)
        if shorten_ipv6:
            ipv6 = shorten_ipv6[0]
            print(ipv6["IPv6"])
        else:
            print("error, while shortening a ipv6 address")
            sys.exit(1)


def output_lenghten_ipv6(args):
    pass