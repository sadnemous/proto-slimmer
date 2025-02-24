import re
import argparse

def extract_messages(proto_file):
    """Extracts and prints message definitions from a .proto file."""
    with open(proto_file, "r") as file:
        content = file.read()

    # Regular expression to match message blocks
    message_pattern = re.findall(r"message\s+(\w+)\s*\{([^}]+)\}", content, re.MULTILINE)

    if not message_pattern:
        print("No messages found in the .proto file.")
        return

    print(f'syntax = "proto3";')
    for message_name, fields in message_pattern:
        print(f"\nmessage: {message_name} {{")
        field_lines = fields.strip().split("\n")
        for field in field_lines:
            field = field.strip()
            if field:  # Ignore empty lines
                print(f"  {field}")
        print(f"}}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract messages from a .proto file.")
    parser.add_argument("proto_file", help="Path to the .proto file")
    args = parser.parse_args()

    extract_messages(args.proto_file)

