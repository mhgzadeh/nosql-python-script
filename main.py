from datetime import datetime

from pymongo import MongoClient
from data import users, projects
from bson.objectid import ObjectId

client = MongoClient()
db = client.clockify_denormalized

users_collection = db.users  # collection in mongodb is equal to table in sql
projects_collection = db.projects
reports_collection = db.reports


def store_once():
    """
    just run at the first of script
    :return:
    """
    user = users_collection.insert_many(users)
    project = projects_collection.insert_many(projects)
    print('Data stored successfully in mongodb')
    print(f"user ids: {user.inserted_ids}\tproject ids: {project.inserted_ids}")


def save_record():
    mohammad = users_collection.find_one({"username": "Mohammad"})
    shop = projects_collection.find_one({"name": "Online shop"})

    report = reports_collection.insert_one({
        'user': mohammad,
        'project': shop,
        'start_time': datetime.now()
    })
    print(report.inserted_id)
    # return report.inserted_id


def set_end_time(object_id):
    query = {'_id': ObjectId(object_id)}
    update = {"$set": {"end_time": datetime.now()}}
    reports_collection.update_one(query, update)
    print('End time set successfully.')


def show_reports():
    for report in reports_collection.find({}):
        duration = report['end_time'] - report['start_time']
        print(f"{report['user']['username']}\t {report['project']['name']}\t {duration}")


if __name__ == "__main__":
    # store_once()
    # save_record()
    # set_end_time('617478797111803175ff1d5d')
    show_reports()
