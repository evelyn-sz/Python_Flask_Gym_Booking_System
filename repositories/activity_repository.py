from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

def save(activity):
    sql = "INSERT INTO activities (name) VALUES (%s) RETURNING id"
    values = [activity.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id
    return activity

def select_all():
    activities = []

    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for row in results:
        activity = Activity(row['name'], row['category'], row['finished'], row['id'])
        activities.append(activity)
    return activities

def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity(result['name'], result['category'], result['finished'], result['id'])
    return activity

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

