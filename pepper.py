import random, string, os, datetime

def create_pepper_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dump{timestamp}.txt"
    lines = [''.join(random.choices(string.ascii_letters + string.digits, k=100)) for _ in range(50)]
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))
    return filename

def main():
    try:
        pepper_filename = "pepper.txt"
        if os.path.exists(pepper_filename):
            os.remove(pepper_filename)
        new_pepper_filename = create_pepper_file()
        os.rename(new_pepper_filename, pepper_filename)
        print(f"New pepper file created: '{pepper_filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
