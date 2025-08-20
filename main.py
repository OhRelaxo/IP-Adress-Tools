from Tools.subnet_calc.calc import exec_subcalc
import argparse

def main():
    parser = argparse.ArgumentParser()
    # write a better help thing
    parser.add_argument("--subcalc", type=str, help="with subcalc (I know horrible name, but that is just how "
                                                    "it goes with programming, I mean what is malloc supposed to mean?)"
                                                    "you can calculate the subnet of a given IP-Address"
                                                    "Input: IP-Address with subnet prefix for example: 192.168.0.1/24")
    args = parser.parse_args()

    if args.subcalc:
        exec_subcalc(args)

if __name__ == '__main__':
    main()