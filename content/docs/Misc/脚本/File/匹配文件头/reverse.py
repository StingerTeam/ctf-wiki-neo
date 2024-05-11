import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="python main.py -f <file_name>")
args  = parser.parse_args()


if __name__ == "__main__":
    file_path = os.path.abspath(args.f)

    if os.path.exists(args.f):
        with open(args.f, "rb") as f:
            file_name = file_path.split("\\")[-1]
            data =  f.read()
    else:
        print("文件不存在!")
        os.system("pause")
        exit(-1)

    # 12 34 56 78 90 AB -> AB 90 87 56 34 12
    with open(f"reverse_1_{file_name}", "wb") as f:
        for i in data[::-1]:
            f.write(i.to_bytes(1, byteorder="big", signed=False))

    # 12 34 56 78 90 AB -> BA 09 87 65 43 21
    with open(f"reverse_2_{file_name}", "wb") as f:
        for i in data[::-1]:
            f.write(((i >> 4) + ((i << 4) & 0xFF)).to_bytes(1, byteorder="big", signed=False))

    # 12 34 56 78 90 AB -> 34 12 78 56 AB 90
    with open(f"reverse_3_{file_name}", "wb") as f:
        for i in range(0, len(data), 2):
            f.write(data[i:i+2][::-1])

    # 12 34 56 78 90 AB -> 43 21 87 65 BA 09
    with open(f"reverse_4_{file_name}", "wb") as f:
        for i in range(0, len(data), 2):
            for j in data[i:i+2][::-1]:
                f.write(((j >> 4) + ((j << 4) & 0xFF)).to_bytes(1, byteorder="big", signed=False))

    # 12 34 56 78 90 AB -> 21 43 65 87 09 BA
    with open(f"reverse_5_{file_name}", "wb") as f:
        for i in data:
            f.write(((i >> 4) + ((i << 4) & 0xFF)).to_bytes(length=1, byteorder="big", signed=False))

    # 12345678 90ABCDEF -> 78563412 efcdab90
    with open(f"reverse_6_{file_name}", "wb") as f:
        for i in range(0, len(data), 4):
            f.write(data[i:i+4][::-1])

    # 12345678 90ABCDEF -> EFCDAB078563412
    with open(f"reverse_7_{file_name}", "wb") as f:
        for i in range(0, len(data), 8):
            f.write(data[i:i+8][::-1])


