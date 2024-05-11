IMAGE = {
    "JPG": {
        "HEAD": ["FF D8 FF DB", "FF 4F FF 51", "FF D8 FF EE", "FF D8 FF E0 00 10 4A 46 49 46 00 01", "FF D8 FF E1 ?? ?? 45 78 69 66 00 00", "FF D8 FF E0"],
        "TAIL": ["FF D9"]
    },
    "PNG": {
        "HEAD": ["89 50 4E 47 0D 0A 1A 0A"],
        "TAIL": ["00 00 00 00 49 45 4E 44 AE 42 60 82"]
    },
    "GIF": {
        "HEAD": ["47 49 46 38 37 61", "47 49 46 38 39 61"],
        "TAIL": ["00 3B"],
    },
    "WEBP": {
        "HEAD": ["52 49 46 46 ?? ?? ?? ?? 57 45 42 50"],
        "TAIL": [],
    },
    "BMP": {
        "HEAD": ["42 4D"],
        "TAIL": [],
    },
    "BPG": {
        "HEAD": ["42 50 47 FB"],
        "TAIL": [],
    },
    "TIF": {
        "HEAD": ["49 49 2A 00"],
        "TAIL": [],
    }
}

COMPRESS = {
    "ZIP/APK/DOCX/XLSX/PPTX": {
        "HEAD": ["50 4B 03 04"],
        "TAIL": ["50 4B 05 06 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??"],
    },
    "RAR v1.5 onwards": {
        "HEAD": ["52 61 72 21 1A 07 00"],
        "TAIL": ["C4 3D 7B 00 40 07 00"],
    },
    "RAR v5.0 onwards": {
        "HEAD": ["52 61 72 21 1A 07 01 00"],
        "TAIL": ["1D 77 56 51 03 05 04 00"]
    },
    "7ZIP": {
        "HEAD": ["37 7A BC AF 27 1C"],
        "TAIL": []
    },
    "ZLIB": {
        "HEAD": ["78 01", "78 5E", "78 9C", "78 DA", "78 20", "78 7D", "78 BB", "78 F9"],
        "TAIL": []
    },
    "BZ2": {
        "HEAD": ["42 5A 68"],
        "TAIL": []
    },
    "GZ/TAR": {
        "HEAD": ["1F 8B"],
        "TAIL": []
    }
}

AUDIO = {
    "MP3": {
        "HEAD": ["FF FB", "FF F3", "FF F2", "49 44 33"],
        "TAIL": []
    },
    "WAV": {
        "HEAD": ["52 49 46 46 ?? ?? ?? ?? 57 41 56 45"],
        "TAIL": []
    },
    "OGG": {
        "HEAD": ["4F 67 67 53"],
        "TAIL": []
    },
}

VIDEO = {
    "MP4": {
        "HEAD": ["?? ?? ?? ?? 66 74 79 70 69 73 6F 6D"],
        "TAIL": []
    },
    "3GP/3G2": {
        "HEAD": ["?? ?? ?? ?? 66 74 79 70 33 67"],
        "TAIL": []
    },
    "MP4/3GP/3G2": {
        "HEAD": ["?? ?? ?? ?? 66 74 79 70"],
        "TAIL": []
    },
    "AVI": {
        "HEAD": ["52 49 46 46 ?? ?? ?? ?? 41 56 49 20"],
        "TAIL": []
    }
}

OTHER = {
    "PDF": {
        "HEAD": ["25 50 44 46 2D"],
        "TAIL": ["25 25 45 4F 46", "25 25 45 4F 46 0A"]
    },
    "DOC/XLS/PPT/MSI/MSG": {
        "HEAD": ["D0 CF 11 E0 A1 B1 1A E1"],
        "TAIL": []
    },
    "MKV/MKA/MKS/MK3D/WEBM": {
        "HEAD": ["1A 45 DF A3"],
        "TAIL": []
    },
    "PCAP": {
        "HEAD": ["D4 C3 B2 A1"],
        "TAIL": []
    },
    "PCAPNG": {
        "HEAD": ["0A 0D 0D 0A"],
        "TAIL": []
    },
    "PST": {
        "HEAD": ["21 42 44 4E"],
        "TAIL": []
    },
    "MRD/MRF": {
        "HEAD": ["8D 84 1E 00 8D 84 1E 00"],
        "TAIL": ["08 00 00 00 24 00 45 00 4E 00 44 00 00 00 00 00"]
    }
}

FILE_DATA = [IMAGE, COMPRESS, AUDIO, VIDEO, OTHER]
