import csv
import sys

def get_arguments():
    if len(sys.argv) < 3:
        print("Usage: python hpf.py <input_file> <output_file>")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        return input_file, output_file

def convert_small_values_to_zero(input_file, output_file, threshold):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)

        # Open the output CSV file for writing.
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)

            # Iterate through the rows in the input file.
            for row in reader:
                # Convert small values to zero based on the threshold.
                modified_row = [float(value) if abs(float(value)) >= threshold else 0.0 for value in row]
                writer.writerow(modified_row)

if __name__ == "__main__":
    input_file_path, output_file_path = get_arguments()
    threshold_value = 0.0001

    convert_small_values_to_zero(input_file_path, output_file_path, threshold_value)

    print(f"Conversion completed. Output saved to '{output_file_path}'.")
