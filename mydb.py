import hashlib
import hmac
import json
import os


class Database:
    def __init__(self, path="db.json"):
        self.path = path
        if not os.path.exists(self.path):
            self._save({})

    def _load(self):
        try:
            with open(self.path, "r") as rf:
                return json.load(rf)
        except json.JSONDecodeError:
            return {}

    def _save(self, data):
        with open(self.path, "w") as wf:
            json.dump(data, wf, indent=4)

    @staticmethod
    def _hash(password, salt):
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode(), bytes.fromhex(salt), 100_000
        ).hex()

    def add_data(self, name, email, password):
        data = self._load()
        if email in data:
            return 0
        salt = os.urandom(16).hex()
        data[email] = [name, self._hash(password, salt), salt]
        self._save(data)
        return 1

    def search(self, email, password):
        data = self._load()
        if email not in data:
            return 0
        _, stored_hash, salt = data[email]
        ok = hmac.compare_digest(self._hash(password, salt), stored_hash)
        return 1 if ok else 0