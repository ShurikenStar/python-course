data = input("Enter some text to write into the file: ")
with open("output.txt", "w") as f:
    f.write(data + "\n")
    print("Data successfully written to output.txt")

more_data = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(more_data + "\n")
    print("Data successfully appended")

# Step 3: Read and display final content
print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())