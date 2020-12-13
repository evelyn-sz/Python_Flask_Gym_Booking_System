from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    activities = member_repository.activities(member)
    return render_template("members/show.html", member = member, activities = activities)

@members_blueprint.route("/members/new")
def new_member():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_member = Member(first_name, last_name)
    member_repository.save(new_member)
    return redirect("/members")