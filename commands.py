from getpass import getpass

class CommandHandler:
    def __init__(self,crypto, storage):
        self.crypto = crypto
        self.storage = storage

    def add(self, account: str, overwrite: bool = False):
        db = self.storage.load_db()
        if account in db and not overwrite:
            print(f"Account '{account}' already exists. Use --overwrite to update it.")
            return
        password = getpass(f"Enter password for '{account}': ")
        confirm = getpass(f"Confirm password for '{account}': ")

        if password != confirm:
            print("Passwords do not match. Please try again.")
            return
        
        db[account] = self.crypto.encrypt(password)
        self.storage.save_db(db)
        print(f"Account '{account}' added successfully.")

    def get(self, account: str, quiet: bool = False):
        db = self.storage.load_db()
        if account not in db:
            print(f"Account '{account}' not found.")
            return
        try:
            password = self.crypto.decrypt(db[account])
        except Exception:
            print(f"Failed to decrypt password for '{account}'.")
            return
        print(password if quiet else f"Password for '{account}': {password}")

    def list_accounts(self):
        db = self.storage.load_db()
        if not db:
            print("No accounts saved/found.")
            return
        print("Saved accounts:")
        for name in db.keys():
            print(f"- {name}")
    def delete(self, account: str):
        db = self.storage.load_db()
        if account not in db:
            print(f"Account '{account}' not found.")
            return
        else:
            del db[account]
            self.storage.save_db(db)
            print(f"Account '{account}' deleted successfully.")
