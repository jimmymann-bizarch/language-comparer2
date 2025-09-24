import pandas as pd
import os

def read_excel_lines(filepath):
    df = pd.read_excel(filepath, engine="openpyxl")
    return [tuple(row) for row in df.values]

def compare_multiple_files(filepaths):
    all_lines = []
    for filepath in filepaths:
        lines = read_excel_lines(filepath)
        all_lines.append(set(lines))

    # Lines that are the same across all files
    same = set.intersection(*all_lines)
    # Lines that are different (appear in some, but not all)
    different = set.union(*all_lines) - same

    return same, different

if __name__ == "__main__":
    # Ask user for the number of files and their paths
    n = int(input("How many Excel files do you want to compare? "))
    filepaths = []
    for i in range(n):
        path = input(f"Enter the path to Excel file #{i+1}: ")
        filepaths.append(path)

    same, different = compare_multiple_files(filepaths)

    # Write results to files
    with open("same.txt", "w") as f:
        f.write("Same rows across ALL files:\n")
        for line in same:
            f.write(str(line) + "\n")

    with open("different.txt", "w") as f:
        f.write("Rows that are different (appear in some, but not all):\n")
        for line in different:
            f.write(str(line) + "\n")

    print("\nComparison complete!")
    print("Results saved to same.txt and different.txt.")
