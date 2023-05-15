import getpass
import pickle

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, site, username, password):
        self.passwords[site] = (username, password)

    def remove_password(self, site):
        del self.passwords[site]

    def get_password(self, site):
        return self.passwords.get(site)

    def save_passwords(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.passwords, f)

    def load_passwords(self, filename):
        with open(filename, 'rb') as f:
            self.passwords = pickle.load(f)

def main():
    pm = PasswordManager()

    while True:
        print("1. Add password")
        print("2. Remove password")
        print("3. Get password")
        print("4. Save passwords")
        print("5. Load passwords")
        print("6. Quit")

        choice = input("Enter choice: ")

        if choice == '1':
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            pm.add_password(site, username, password)
        elif choice == '2':
            site = input("Enter site: ")
            pm.remove_password(site)
        elif choice == '3':
            site = input("Enter site: ")
            login_info = pm.get_password(site)
            if login_info:
                print("Site: {}".format(site))
                print("Username: {}".format(login_info[0]))
                print("Password: {}".format(login_info[1]))
            else:
                print("Site not found")
        elif choice == '4':
            filename = input("Enter filename: ")
            pm.save_passwords(filename)
        elif choice == '5':
            filename = input("Enter filename: ")
            pm.load_passwords(filename)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
