def write_file(content):
    with open("hi.txt", "w", encoding="UTF-8") as f:
        f.write(content)
    return content

if __name__ == "__main__":
    write_file( "This is intended!")