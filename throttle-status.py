import subprocess
import sys

from blessed import Terminal

term = Terminal()

hex2bin_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

err_map = {
    0: "soft temperature reached since last reboot",
    1: "arm frequency capped has occurred since last reboot",
    2: "throttling has occurred since last reboot",
    3: "soft temperature reached",
    16: "soft temperature reached",
    17: "arm frequency capped",
    18: "currently throttled",
    19: "under-voltage",
}


def parse_hex_value(value):
    result = str()
    for i in value:
        result = result + (hex2bin_map.get(i.upper()))
    return result


def process_binary_status(binary):
    print("\n" + binary)
    rows = 0

    errs = {}
    for i in range(len(binary)):
        if binary[i] == "1":
            errs[i] = err_map.get(i)
            rows += 1

    for i in range(rows):
        result = ""
        for j in range(len(binary)):
            if binary[j] == "1":
                if j == max(errs.keys()):
                    result = result + "|_" + str(errs.get(j))
                    break
                else:
                    result = result + "|"
            else:
                result = result + " "
        errs.pop(max(errs.keys()))
        print(result)
    print("\n")


def print_help():
    print("Press q to quit", end='')
    sys.stdout.flush()


def main():
    with term.fullscreen(), term.cbreak():
        val = ''
        while val.lower() != 'q':
            # Clear terminal between runs
            term.clear()
            
            print_help()
            val = term.inkey()

            if not val:
                process = subprocess.Popen(["vcgencmd", "get_throttled"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                process.wait()
                output = process.stdout.read()
                rc = process.returncode

                if rc == 0:
                    response = output.strip().split(b'=')[1][2:]
                    process_binary_status(parse_hex_value(response))
                else:
                    print("An error occurred while fetching system status.")


if __name__ == "__main__":
    main()
