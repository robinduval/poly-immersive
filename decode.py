import sys
import re

def decode_byte_string(bytes_string, content):
        bytes_array_string = bytes_string.split()
        bytes_array_int = [int(i) for i in bytes_array_string]
        for split in bytes_array_string:
	        content += ("{:02x}".format(int(split)))

def parse_file(file_path):
        content = []
        file = open(file_path, "r")
        lines = file.readlines()
        
        for line in lines:
                RegexMatches = re.search('    WriteBytes objFile, "([\d ]+)"', line)
                if RegexMatches:
                        bytes_string = RegexMatches.group(1)
                        decode_byte_string(bytes_string, content)
        print("".join(content))
        file.close()
parse_file(sys.argv[1])
