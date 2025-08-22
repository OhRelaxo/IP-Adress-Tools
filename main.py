from Tools.subnet_calc.calc import output_subcalc
from Tools.ip_conversion.ipv4_to_ipv6 import output_ip4to6
import argparse

def main():
    parser = argparse.ArgumentParser()
    # write a better help thing, I think it should be good now :)
    parser.add_argument("--subcalc", type=str, help="with subcalc (I know horrible name, but that is just how "
                                                    "it goes with programming, I mean what is malloc supposed to mean?)"
                                                    "you can calculate the subnet of a given IP-Address"
                                                    "Input: IP-Address with subnet prefix for example: 192.168.0.1/24"
                                                    "other supported flags: --export and also --verbose with it")
    parser.add_argument("--export", choices=["csv", "json"], help="exports a subcalc as a csv or json. "
                                                                  "Input: write --<one of the supported arguments> --export csv or json"
                                                                  "currently only subcalc is supported")
    parser.add_argument("--verbose", action="store_true", help="will also output the subcalc table or the iv6 address "
                                                               "if --import is used in the commandline, "
                                                              "can only be used with the --export/--import flag!")
    parser.add_argument("--ip4to6", type=str, help="with ip4to6 you can convert an ipv4 address to an ipv6 address."
                                                   "Input: --ipv4to6 <IP-Address> (e.g.: 192.168.0.1) without a subnet prefix!")
    parser.add_argument("--input", type=str, help="is used to read from a csv file, for the ip4to6 conversion "
                                                                  "and it will also write the output into a csv file, "
                                                                  "note: it uses the first row, so u need to put the ipv4 addresses that you "
                                                                  "want to convert to ipv6 address into the first row! Also if you want the"
                                                                  "converted address to get output into the commandline you can use the"
                                                                  "--verbose flag."
                                                  "how to use: --ip4to6 --input<file_name> the file has to be in the directory of the code!")
    args = parser.parse_args()


    if args.subcalc:
        output_subcalc(args)

    if args.ip4to6:
        output_ip4to6(args)

if __name__ == '__main__':
    main()