#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'emma@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

#auth.register_user(email, password)

#print(auth.create_session(email))
#print(auth.create_session("unknown@email.com"))
user = auth.get_user_from_session_id(session_id="5dd7787c-7971-4b47-8fa5-b86a48e32e15")
print()