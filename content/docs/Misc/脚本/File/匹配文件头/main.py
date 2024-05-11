import os
import binascii
import argparse
from data import FILE_DATA
from collections import Counter
from rich.console import Console


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="python main.py -f <file_name>")
args  = parser.parse_args()

file_dir = os.getcwd()
console = Console()

def get_max_bytes(FILE_DATA, dict_key):
    # sourcery skip: for-append-to-extend, inline-variable
    numbers = []
    for file_class in FILE_DATA:
        for value in file_class.values():
            if value[dict_key] != []:
                number = sum(i != " " for i in max(value[dict_key]))
                numbers.append(number)
    return max(numbers)

def bytes_to_hexstr(bytes):
    # b'\xff\xfb' -> b'fffb' -> 'fffb'
    hex_str = binascii.b2a_hex(bytes).decode()
    return ' '.join(hex_str[i:i+2].upper() for i in range(0, len(hex_str), 2))

def get_hex_str(max_head_bytes, max_tail_bytes):
    with open(args.f, "rb") as f:
        data = f.read()
    return bytes_to_hexstr(data[:max_head_bytes]), bytes_to_hexstr(data[-max_tail_bytes:])

def get_similarity(record_hexstr, file_hexstr, reverse=False):
    byte, total_bytes = 0, 0
    if reverse:
        record_hexstr = record_hexstr[::-1]
        file_hexstr = file_hexstr[::-1]

    for i in range(len(record_hexstr)):
        if record_hexstr[i] not in [" ", "?"]:
            total_bytes += 1
            if record_hexstr[i] == file_hexstr[i]:
                byte += 1
    return round(byte / total_bytes, 4)

def compare(file_hexstr, dict_key):
    print_info = []
    for file_class in FILE_DATA:
        for file_type, value in file_class.items():
            for record_hexstr in value[dict_key]:
                if dict_key == "HEAD":
                    if (similarity := get_similarity(record_hexstr, file_hexstr)) > 0.5:
                        print_info.append([file_type, record_hexstr, similarity])
                elif dict_key == "TAIL":
                    if (similarity := get_similarity(record_hexstr, file_hexstr, reverse=True)) > 0.5:
                        print_info.append([file_type, record_hexstr, similarity])
    return dict_key, print_info

def show_info(dict_key, print_info):
    print_info = sorted(print_info, key=lambda x: x[-1], reverse=True)
    for info in print_info:
        file_type, record_hexstr, similarity = info
        if dict_key == "HEAD":
            console.print(f"[bold red]类型: [/]{file_type}, [bold red]对比文件头: [/]{record_hexstr}, [bold red]文件头相似度: [/]{similarity}", style="bold cyan")
        elif dict_key == "TAIL":
            console.print(f"[bold red]类型: [/]{file_type}, [bold red]对比文件尾: [/]{record_hexstr}, [bold red]文件尾相似度: [/]{similarity}", style="bold cyan")

def get_notstr(file_hexstr):
    file_hexstr = file_hexstr.split(" ")
    return ' '.join([hex((256 - int(hex_str, 16)) % 256)[2:].zfill(2).upper() for hex_str in file_hexstr])

def show_not_info(dict_key, print_info):
    print_info = sorted(print_info, key=lambda x: x[-1], reverse=True)
    for info in print_info:
        file_type, record_hexstr, similarity = info
        if dict_key == "HEAD":
            console.print(f"[bold red]类型: [/]{file_type}, [bold red]求反文件头: [/]{record_hexstr}, [bold red]文件头相似度: [/]{similarity}", style="bold cyan")
        elif dict_key == "TAIL":
            console.print(f"[bold red]类型: [/]{file_type}, [bold red]求反文件尾: [/]{record_hexstr}, [bold red]文件尾相似度: [/]{similarity}", style="bold cyan")

def get_xor_similarity(record_hexstr, file_hexstr, reverse=False):
    if reverse:
        record_hexstr = record_hexstr[::-1]
        file_hexstr = file_hexstr[::-1]

    record_hexstr = record_hexstr.split(" ")
    file_hexstr = file_hexstr.split(" ")
    if reverse is False:
        xor_ret = [hex(int(record_hexstr[i], 16) ^ int(file_hexstr[i], 16)) for i in range(len(record_hexstr)) if record_hexstr[i] != "??"]
    else:
        xor_ret = [hex(int(record_hexstr[i][::-1], 16) ^ int(file_hexstr[i][::-1], 16)) for i in range(len(record_hexstr)) if record_hexstr[i] != "??"]
    result = Counter(xor_ret).most_common()
    return result[0][0], round(result[0][1] / len(xor_ret), 4)

def xor_compare(file_hexstr, dict_key):
    print_info = []
    for file_class in FILE_DATA:
        for file_type, value in file_class.items():
            for record_hexstr in value[dict_key]:
                if dict_key == "HEAD":
                    xor_hex, xor_similarity = get_xor_similarity(record_hexstr, file_hexstr)
                    if xor_similarity > 0.5:
                        print_info.append([file_type, record_hexstr, xor_hex, xor_similarity])
                elif dict_key == "TAIL":
                    xor_hex, xor_similarity = get_xor_similarity(record_hexstr, file_hexstr, reverse=True)
                    if xor_similarity > 0.5:
                        print_info.append([file_type, record_hexstr, xor_hex, xor_similarity])
    return dict_key, print_info

def show_xor_info(dict_key, print_info):
    print_info = sorted(print_info, key=lambda x: x[-1], reverse=True)
    for info in print_info:
        file_type, record_hexstr, xor_str, xor_similarity = info
        if dict_key == "HEAD":
            console.print(f"[bold red]类型: [/]{file_type}, [bold red]异或文件头: [/]{record_hexstr}, [bold red]异或: [/]{xor_str}, [bold red]文件头相似度: [/]{xor_similarity}", style="bold cyan")
        elif dict_key == "TAIL":
            console.print(f"[bold red]类型: [/]{file_type}, [bold red]异或文件尾: [/]{record_hexstr}, [bold red]异或: [/]{xor_str}, [bold red]文件尾相似度: [/]{xor_similarity}", style="bold cyan")


if __name__ == "__main__":
    max_head_bytes, max_tail_bytes = get_max_bytes(FILE_DATA, "HEAD"), get_max_bytes(FILE_DATA, "TAIL")
    head_hexstr, tail_hexstr = get_hex_str(max_head_bytes, max_tail_bytes)

    console.print("Byxs20's File Format Tools", style="bold magenta")
    # 1.检测文件头和文件尾
    flag = None
    console.print("1.开始检测文件头和文件尾:", style="bold blue")
    for file_hexstr, dict_key in [(head_hexstr, "HEAD"), (tail_hexstr, "TAIL")]:
        dict_key, print_info = compare(file_hexstr=file_hexstr, dict_key=dict_key)
        if print_info != []:
            flag = True
            show_info(dict_key, print_info)
    if not flag:
        console.print("没有检测到符合的文件头和文件尾!", style="bold red")
    
    # 2.求反文件头和文件尾
    flag = None
    console.print("\n2.开始取反文件头和文件尾:", style="bold blue")
    for file_hexstr, dict_key in [(head_hexstr, "HEAD"), (tail_hexstr, "TAIL")]:
        dict_key, print_info = compare(file_hexstr=get_notstr(file_hexstr), dict_key=dict_key)
        if print_info != []:
            flag = True
            show_info(dict_key, print_info)
    if not flag:
        console.print("没有取反到符合的文件头和文件尾!\n", style="bold red")

    # 3.异或文件头和文件尾
    flag = None
    console.print("\n3.开始异或文件头和文件尾:", style="bold blue")
    for file_hexstr, dict_key in [(head_hexstr, "HEAD"), (tail_hexstr, "TAIL")]:
        dict_key, print_info = xor_compare(file_hexstr=file_hexstr, dict_key=dict_key)
        if print_info != [] and print_info[0][2] != "0x0":
            flag = True
            show_xor_info(dict_key, print_info)
    if not flag:
        console.print("没有异或到符合的文件头和文件尾!", style="bold red")

    os.system("pause")