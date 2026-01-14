try:
    with open("sample.txt","r") as fh:
        print("Reading file content:")
        print(fh.read())

except FileNotFoundError:
    print(f"Error: The file {'sample.txt'} is not found")

