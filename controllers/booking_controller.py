from flask import Flask, flash, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

import pdb

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/<id>")
def show(id):
    booking = booking_repository.select(id)
    return render_template("bookings/show.html", booking = booking)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("bookings/new.html", members = members, activities = activities)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    member = member_repository.select(member_id)
    activity_id = request.form["activity_id"]
    activity = activity_repository.select(activity_id)
    new_booking = Booking(member, activity)
    if booking_repository.save(new_booking) is not None:
        return redirect("/bookings")
    else:
        return render_template("/bookings/full.html")

@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("bookings/edit.html", booking=booking, members=members, activities=activities)

@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    booking = Booking(member, activity, id)
    booking_repository.update(booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

#below, code for finishing second extension

# @bookings_blueprint.route("/bookings", methods=["POST"])
# def create_booking():
#     member_id = request.form["member_id"]
#     member = member_repository.select(member_id)
#     activity_id = request.form["activity_id"]
#     activity = activity_repository.select(activity_id)
#     new_booking = Booking(member, activity)
#     if booking_repository.save(new_booking) == False:
#         return render_template("/bookings/membership_error.html")
#         # pdb.set_trace()
#     elif booking_repository.save(new_booking) == None:
#         return render_template("/bookings/full.html")
#     elif booking_repository.save(new_booking) is not None:
#         return redirect("/bookings")


    # if booking_repository.save(new_booking) is not None:
    #     return redirect("/bookings")
    # else:
    #     return render_template("/bookings/full.html")
