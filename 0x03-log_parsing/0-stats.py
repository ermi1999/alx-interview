#!/usr/bin/python3
"""module for parsing log."""
import sys

if __name__ == "__main__":
    file_size = 0
    status_codes = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
    }
    i = 0
    try:
        for line in sys.stdin:
            splited = line[: -1].split(" ")
            if len(splited) != 9:
                continue
            if splited[-2] not in status_codes.keys():
                continue
            if not splited[-1].isdigit():
                continue
            if len(splited[0].split('.')) != 4:
                continue
            if splited[1] != '-':
                continue
            if len(splited[2].split('-')) != 3:
                continue
            if (f'{splited[4]} {splited[5]} {splited[6]}'
                != '"GET /projects/260 HTTP/1.1"'):
                continue
            status_codes[splited[-2]] += 1
            file_size += int(splited[-1])
            i += 1

            if i % 10 == 0:
                print(f'File size: {file_size}')
                for key, value in status_codes.items():
                    if value == 0:
                        continue
                    print(f'{key}: {value}')
    finally:
        print(f'File size: {file_size}')
        for key, value in status_codes.items():
            if value == 0:
                continue
            print(f'{key}: {value}')
