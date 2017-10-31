# -*- coding:utf-8 -*-

from app import app, db, auth
from flask import render_template, json, jsonify, request, abort, g
from app.models import *

@app.route("/")
@auth.login_required
def index():    
    return jsonify('Hello, %s' % g.user.username)


@app.route('/api/register', methods = ['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username })

@auth.verify_password
def verify_password(username_or_token, password):
    if request.path == "/api/login":
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    else:
        user = User.verify_auth_token(username_or_token)
        if not user:
            return False    
    g.user = user   
    return True


@app.route('/api/login')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify(token)

