import bcrypt
from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt


@app.route("/send_message", methods=["POST"])
def send_message():
    if("user_id" not in session):
        return redirect("/")
    else:
        Message.save(request.form)
        return redirect("/wall")


@app.route("/delete/message/<int:id>")
def delete_message(id):
    form={"id":id}
    Message.delete(form)
    return redirect("/wall")