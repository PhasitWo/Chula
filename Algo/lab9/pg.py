def readInput(file_path):
    with open("Algo/lab9/9.1.txt", "r") as openfile:
        sigma = openfile.readline().strip()
        pattern_length, text_length = list(map(int, openfile.readline().strip().split()))
        pattern = openfile.readline().strip()
        text = openfile.readline().strip()
    return text, pattern