from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values= [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result ['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "SELECT members SET ( first_name = %s, last_name ) = (%s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.id]
    run_sql(sql, values)

def activities(member):
    activities = []
    sql = "SELECT activities.* FROM activities INNER JOIN bookings ON bookings.activity_id = activities.id WHERE bookings.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        activity = Activity(row['name'], row['venue'], row['category'], row['finished'], row['id'])
        activities.append(activity)
    return activities