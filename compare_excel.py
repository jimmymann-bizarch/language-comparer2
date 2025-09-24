import pandas as pd

def read_excel_lines(filepath):
    # Read the Excel file into a dataframe
    df = pd.read_excel(filepath, engine="openpyxl")
    # Convert each row to a tuple (for easy comparison)
    return [tuple(row) for row in df.values]

def compare_files(file1, file2):
    # Read lines from both files
    lines1 = read_excel_lines(file1)
    lines2 = read_excel_lines(file2)

    # Find lines that are the same
    same = [line for line in lines1 if line in lines2]

    # Find lines that are different (in either file, but not both)
    different = list(set(lines1 + lines2) - set(same))

    return same, different

if __name__ == "__main__":
    # Example usage
    file1 = input("Enter the path to the first Excel file: ")
    file2 = input("Enter the path to the second Excel file: ")

    same, different = compare_files(file1, file2)

    print("\n=== Same ===")
    for line in same:
        print(line)

    print("\n=== Different ===")
    for line in different:
        print(line)
