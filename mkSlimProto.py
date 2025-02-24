import re
import sys

def extract_proto_info(proto_file):
    with open(proto_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    output = []
    inside_message = False
    brace_cnt = 0
    pad = ""

    for line in lines:
        stripped = line.strip()
        arr = re.split('\s+', stripped)
        # join the array into a string
        stripped_2 = ' '.join(arr)
        # Capture syntax
        if stripped_2.startswith('syntax = "proto'):
            output.append(stripped_2)

        # Capture package declaration
        elif stripped_2.startswith("package "):
            output.append(stripped_2)

        # Capture java options
        elif stripped_2.startswith("option java_"):
            output.append(stripped_2)

        # Capture message definitions
        elif stripped_2.startswith("message "):
            inside_message = True
            output.append(f"{stripped_2}")
            brace_cnt = brace_cnt + 1
            pad = f"{pad}  "


        elif inside_message:
            if stripped.count("{") > 0 : 
                brace_cnt = brace_cnt + 1
                pad = f"{pad}  "
            if stripped.count("}") > 0:  # Message block ends
                brace_cnt = brace_cnt - 1
                pad = pad[0:-2]
                if brace_cnt == 0:
                    inside_message = False
            output.append(f"{pad}{stripped}")

    return "\n".join(output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_proto_info.py <proto_file>")
        sys.exit(1)

    proto_file = sys.argv[1]
    extracted_info = extract_proto_info(proto_file)
    
    print("\nExtracted Proto Information:\n")
    print(extracted_info)

