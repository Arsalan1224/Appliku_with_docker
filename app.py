import os
from helper import greet

def main():
    app_name = os.getenv('APP_NAME', 'DefaultApp')
    print(f"Welcome to {app_name}!")
    greet()

if __name__ == '__main__':
    main()
