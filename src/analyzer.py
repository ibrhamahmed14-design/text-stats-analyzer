def analyze_string(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for line in content.splitlines():
                print(len(line))
    except FileNotFoundError:
        print(f"File not found: {file_path}")