import random

from pymongo import MongoClient

client = MongoClient()
db = client.users_data

users_records_collection = db.users


def import_users_data(count=100000):
    for i in range(count):
        users_records_collection.insert_one(
            {f"user_{i}": random.randint(1, 10)}
        )

    print(f"{count} user records imported successfully.")


if __name__ == "__main__":
    import_users_data()
