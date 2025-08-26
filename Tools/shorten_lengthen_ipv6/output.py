import sys
from Tools.input_export import input_csv, export_csv
from Tools.shorten_lengthen_ipv6.lengthen import create_long_ipv6
from Tools.shorten_lengthen_ipv6.shorten import create_shorten_ipv6


def output_shorten_ipv6(args):
    output_ipv6("shorten_ipv6", create_shorten_ipv6, args)

def output_lenghten_ipv6(args):
    output_ipv6("expand_ipv6", create_long_ipv6, args)

def output_ipv6(args_type, func, args):
    if args.output_format:
        print(f"error: --export is not support with {args_type} for help see -h or --help")
        sys.exit(1)
    if args.verbose and not args.input_file:
        print(f"error: you can only use verbose with the --output-format or the --input-file flag! for help see -h or --help")
        sys.exit(1)

    if args.input_file:
        print("converting...")
        ipv6_list = func(input_csv(args))
        export_csv(ipv6_list, f"{args_type}.csv", ["IPv6"])
        if args.verbose:
            for ipv6 in ipv6_list:
                print(ipv6["IPv6"])
    else:
        if args.expand_ipv6:
            ip_adr = [args.expand_ipv6]
        else:
            ip_adr = [args.shorten_ipv6]
        finished_ipv6 = func(ip_adr)
        if finished_ipv6:
            ipv6 = finished_ipv6[0]
            print(ipv6["IPv6"])
        else:
            print("error, while lengthening a ipv6 address")
            sys.exit(1)