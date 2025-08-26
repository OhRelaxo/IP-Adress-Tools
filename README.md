# IP-Adress-Tools
A CLI tool for calculating subnets of IPv4 addresses, converting IPv4 to IPv6 addresses, and shortening or lengthening IPv6 addresses.

## Installation Guide
1. install python from the website or your favorite packet manager
2. use `git clone https://github.com/OhRelaxo/IP-Adress-Tools` to clone the repository into a directory
3. optional: create a venv `python3 -m venv .venv` or `python -m venv .venv`
4. activate your virtual environment, for this there are scripts in the repository, you can also use this command: on Windows: `.venv\Scripts\activate` on Linux/macOS: `source .venv/bin/activate`
5. install the dependencies using the requirements.txt `pip install -r requirements.txt`
6. now you can run the main.py file with either: `python ./main.py` or `python3 ./main.py`

## How to use
### calculating subnets of IPv4 Addresses
for calculating subnets there is the `--subnet` or `s` flag, it takes an 
IP-Address with subnet prefix e.g. 192.168.0.1/28 as intput.
It can be used with the`--output-format` or `o` flag, it takes two formats as 
arguments: csv or json and outputs a file with the generated subnets according 
to the format, there is also a `--verbose` or `-v` flag for also outputting 
the generated subnet in the console.

#### Here are some examples of using the `--subnet` flag
````commandline
python3 ./main.py --subnet 172.31.1.1/18 --output-format csv
````

### converting IPv4 Addresses to IPv6 Addresses

### shortening / lengthening IPv6 Addresses
