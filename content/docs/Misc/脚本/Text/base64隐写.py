import base64
import codecs


def get_base64_diff_value(s1, s2):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = 0
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            return abs(base64chars.index(chr(s1[i])) - base64chars.index(chr(s2[i])))
    return res


def solve_stego():
    with open('C:\\CTF\\temp\\ComeOn!.txt', 'rb') as f:
        file_lines = f.readlines()
        bin_str = ''
        for line in file_lines:
            steg_line = line.replace(b'\n', b'')
            norm_line = base64.b64encode(
                base64.b64decode(steg_line)).replace(b'\n', b'')
            diff = get_base64_diff_value(steg_line, norm_line)
            print(diff)
            pads_num = steg_line.count(b'=')
            if diff:
                bin_str += bin(diff)[2:].zfill(pads_num * 2)
            else:
                bin_str += '0' * pads_num * 2
            print(goflag(bin_str))


def goflag(bin_str):
    res_str = ''
    for i in range(0, len(bin_str), 8):
        res_str += chr(int(bin_str[i:i + 8], 2))
    return res_str


if __name__ == '__main__':
    solve_stego()
