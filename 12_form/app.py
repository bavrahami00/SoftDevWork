#Saad Bhuiyan and Benjamin Avrahami
#SoftDev1 pd2
#K12 -- Echo Echo Echo 
#2019-09-27 

from flask import Flask, render_template, request
app = Flask(__name__)

teamName = "Team Puppy Adoption"
teamMembers = "Saad Bhuiyan and Benjamin Avrahami"

@app.route("/")
def form():
    print(app)
    return render_template("form.html", 
                            teamName = teamName,
                            teamMembers = teamMembers
    )

@app.route("/auth")
def authenticate():
    print("\n\n")
    print("*** DIAG: this Flask obj***")
    print(app)
    print("*** DIAG: request obj ****")
    print(request)
    print("*** DIAG: request.method ****")
    print(request.method)
    print("*** DIAG: request.headers ****")
    print(request.headers)
    print("*** DIAG: request.form ****")
    print(request.form)
    print("*** DIAG: request.args ****")
    print(request.args)
    print("\n\n")
    return render_template("response.html", 
                            teamName = teamName,
                            teamMembers = teamMembers,
                            type = request.method,
                            name = request.args['name'],
                            donation = request.args['donation']
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
