def save_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data + "\n")