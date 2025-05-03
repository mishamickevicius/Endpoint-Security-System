import hashlib

def compute_file_hash(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in chunks of 8192 bytes
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def main():
    file_path = input("Enter the path to the file: ")
    file_hash = compute_file_hash(file_path)
    print(file_hash)

if __name__ == '__main__':
    main()

