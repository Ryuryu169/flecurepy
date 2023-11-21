import sys
from encrypt.encrypt_file import encrypt
from auth.auth import auth

if __name__ == "__main__":
    # Authenticate user by github username and password
    # If user is not authenticated, exit the program
    # If user is authenticated, continue to encrypt the file

    authSituation = auth()

    if authSituation == None:
        exit()

    # Encrypt the file
    encrypt(authSituation)
    print("Done!")
