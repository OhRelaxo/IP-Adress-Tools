from Tools.subnet_calc.calc import exec_subcalc
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
    parser.add_argument("--verbose", action="store_true", help="will also output the subcalc table in the commandline, "
                                                              "can only be used with the --export flag!")

    args = parser.parse_args()


    if args.subcalc:
        exec_subcalc(args)

if __name__ == '__main__':
    main()