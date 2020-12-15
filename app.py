from flask import Flask, render_template

from controllers.booking_controller import bookings_blueprint
from controllers.activity_controller import activities_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)
app.secret_key = b'testing_capacity'

app.register_blueprint(bookings_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)