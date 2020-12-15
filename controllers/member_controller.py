from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

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
    membership_type = request.form['membership_type']
    new_member = Member(first_name, last_name, membership_type)
    member_repository.save(new_member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    membership_type = request.form["membership_type"]
    member = Member(first_name, last_name, membership_type, id)
    member_repository.update(member)
    return redirect("/members")