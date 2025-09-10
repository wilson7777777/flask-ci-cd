from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database from an environment variable
# This URL will be provided by Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# A simple database model for storing user entries
class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(80), unique=False, nullable=False)

@app.route("/")
def hello():
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Add a new entry to the database
    new_entry = Entry(message="Hello from Flask!")
    db.session.add(new_entry)
    db.session.commit()

    # Count the total entries and display a message
    total_entries = Entry.query.count()
    return f"<h1>Successfully added a new entry to the database! Total entries: {total_entries}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000

