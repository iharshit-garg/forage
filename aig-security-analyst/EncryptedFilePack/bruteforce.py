from zipfile import ZipFile, BadZipFile
import sys

# Attempt to extract the zip file using a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning brute-force attack on ZIP file...")

    try:
        with ZipFile('enc.zip') as zf:
            with open('rockyou.txt', 'rb') as f:
                for line in f:
                    password = line.strip()  # remove newline and spaces
                    if attempt_extract(zf, password):
                        print(f"[+] Password found: {password.decode('utf-8')}")
                        return
                    else:
                        print(f"[-] Attempt failed: {password.decode('utf-8')}")
    except FileNotFoundError:
        print("[-] File not found. Please ensure 'enc.zip' and 'rockyou.txt' are in the same directory.")
        sys.exit(1)
    except BadZipFile:
        print("[-] Invalid or corrupt zip file.")
        sys.exit(1)

    print("[!] Password not found in the list.")

if __name__ == "__main__":
    main()