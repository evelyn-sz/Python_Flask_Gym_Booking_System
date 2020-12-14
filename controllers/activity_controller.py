from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities = activities)

@activities_blueprint.route("/activities/<id>")
def show(id):
    activity = activity_repository.select(id)
    members = activity_repository.members(activity)
    return render_template("activities/show.html", activity = activity, members = members)

@activities_blueprint.route("/activities/new")
def new_activity():
    return render_template("/activities/new.html")

@activities_blueprint.route("/activities", methods=["POST"])
def create_activity():
    name = request.form["name"]
    venue = request.form["venue"]
    category = request.form["category"]
    finished = request.form["finished"]
    new_activity = Activity(name, venue, category, finished)
    activity_repository.save(new_activity)
    return redirect("/activities")

@activities_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    activity = activity_repository.select(id)
    return render_template('activities/edit.html', activity=activity)

@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    venue = request.form["venue"]
    category = request.form["category"]
    finished = request.form["finished"]
    activity = Activity(name, venue, category, finished, id)
    activity_repository.update(activity)
    return redirect("/activities")
