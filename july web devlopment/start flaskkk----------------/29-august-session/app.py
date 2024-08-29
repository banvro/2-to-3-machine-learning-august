from flask import Flask, session, make_response, request

app = Flask(__name__)

app.secret_key = "sldknadkad adiuadhqw8e8dasdn"

@app.route("/")
def home():
    # session["name"] = "kriss moris"
    # return "session done...."

    # cookies
    resp = make_response("cookies set")
    resp.set_cookie("token", "tokensettttt")
    return resp



@app.route("/get_data")
def getiing():
    # x = session.get("name")
    
    # if x:
    #     return "user login"
    # else:
    #     return "user not login.."

    y = request.cookies.get("token")
    return y

    
@app.route("/delete")
def removesession():
    session.pop("name")
    return "session end"

if __name__ == "__main__":
    app.run(debug = True)



# session store 
    # set session ---> session["key"] = "value"
    # get session ----> session.get("key")
    # delete session ----> session.pop("key")



