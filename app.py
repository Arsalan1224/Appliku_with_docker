# Print environment variables along with text at the output
import os
from helper import greet

def main():
    app_name = os.getenv('APP_NAME', 'DefaultApp')
    print(f"Welcome to {app_name}!")
    
    # Print all environment variables
    print("Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
    
    greet()

if __name__ == '__main__':
    main()
