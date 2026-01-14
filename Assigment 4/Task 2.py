user = input("Enter text to write to the file: ")

with open("output.txt", "wt") as fh:
    fh.write(user + "\n")
    print("Data successful write to output.txt")

i= input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(i)
    print("Data successfully append.")

with open("output.txt", "rt") as t:
    print(f"Final content of output.txt \n{t.read()}")
    