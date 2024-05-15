from bottle import run, get, view, post, request, redirect, response
import uuid

users = [
    {"id":"1",
     "name":"a",
     "last_name": "aa",
     "email": "a@a.com",
     "password": "pass1"
     },
     {"id":"2",
     "name":"b",
     "last_name": "bb",
     "email": "b@b.com",
     "password": "pass2"
     },
]

sessions = {}


# ###################
@get("/login")
@view("login")
def _():
    return

####################
@post("/login")
def _():
    # This is how you grab the name value from your HTML forms page 
    # in this case we grab name values "user_email" and "user_password" from login.html
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    # this is to check if the values are a match

    for user in users:
        if user_email == user["email"] and user_password == user["password"]:
            user_session_id = str(uuid.uuid4())
            sessions[user_session_id] = user
            print("#"*30)
            print(sessions)
            response.set_cookie("user_session_id", user_session_id)
            # if the values are a match, the user is to the admin page endpoint
            return redirect("/admin")
        
    # if the values are not a match, the user is sent back to the login page endpoint
    return redirect("/login")

@get("/admin")
@view("admin")
def _():
    user_session_id = request.get_cookie("user_session_id")
    user = sessions[user_session_id]
    return dict(user=user)


####################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)