import argparse
parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

with open(args.input, "r", encoding="utf-8") as  input_file:
    with open(args.output, "w", encoding="utf-8") as output_file:

        for line in input_file:
            line = line.strip().lower()

            if line:
                output_file.write(line + "\n")