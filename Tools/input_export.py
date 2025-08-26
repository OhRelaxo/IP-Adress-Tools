import csv
import sys
import os
import json

def export_csv(data, file_name, fieldnames):
    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"failed to create the csv, error: {e}")
        sys.exit(1)

def export_json(data, file_name):
    try:
        with open(file_name, mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"failed to create the json file, error: {e}")
        sys.exit(1)

def input_csv(args):
    ip_adr = []
    working_dir = os.getcwd()
    file_path = os.path.join(working_dir, args.input_file)
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            next(reader)
            for row in reader:
                ip_adr.append(row[0])
    except Exception as e:
        print(f"error: failed to read csv file: {e}")
        sys.exit(1)
    return ip_adr
