import os
import hashlib
import argparse


def default_desktop():
    """Return the path to the user's Desktop on the current OS."""
    if os.name == "nt":
        return os.path.join(os.environ.get("USERPROFILE", os.path.expanduser("~")), "Desktop")
    return os.path.expanduser("~/Desktop")


def hash_file(path, chunk_size=8192):
    """Return the SHA-256 hash of a file."""
    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()


def find_duplicates(directory):
    """Yield lists of duplicate files in the directory."""
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                file_hash = hash_file(file_path)
            except (OSError, PermissionError):
                # Skip files that can't be read
                continue
            hashes.setdefault(file_hash, []).append(file_path)

    for file_list in hashes.values():
        if len(file_list) > 1:
            yield file_list


def main():
    parser = argparse.ArgumentParser(description="Find duplicate files.")
    parser.add_argument(
        "directory",
        nargs="?",
        default=default_desktop(),
        help="Directory to search (defaults to your Desktop)",
    )
    args = parser.parse_args()
    target_dir = os.path.abspath(args.directory)

    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory")
        return

    duplicates_found = False
    for dup_group in find_duplicates(target_dir):
        duplicates_found = True
        print("Duplicate files:")
        for path in dup_group:
            print("  ", path)
        print()

    if not duplicates_found:
        print("No duplicates found in", target_dir)


if __name__ == "__main__":
    main()
