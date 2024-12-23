#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST login
    Return:
      - list of all User objects JSON represented
    """
    user_email = request.form.get("email")
    if not user_email:
        return jsonify({"error":"email missing"}), 400
    
    user_password = request.form.get("password")
    if not user_password:
        return jsonify({"error":"password missing"}), 400
    
    try:
        found_users = User.search({'email': user_email})
        if not found_users or found_users == []:
            return jsonify({"error": "no user found for this email"}), 404
   
    except Exception:
        return jsonify({ "error": "no user found for this email" }), 404
    
    valid_user = None

    for user in found_users:
        if user.is_valid_password(user_password):
            valid_user = user
    
    if valid_user is None:
         return jsonify({ "error": "wrong password" }), 401
    else:
         from api.v1.app import auth
         session_id = auth.create_session(valid_user.id)
         session_name = getenv("SESSION_NAME")

         response = jsonify(valid_user.to_json())
         response.set_cookie(session_name, session_id)
         return response

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def handle_logout():
    """
    Handle user logout
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
