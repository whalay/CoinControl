import getpass
from datetime import datetime
from flask.cli import FlaskGroup

from coincontrol.models import Users, db
from wsgi import app

cli = FlaskGroup(app)

@cli.command("create_admin")
def create_admin():
    """Creates an admin user."""
    print("Creating an Admin user...")
    print("Press Ctrl-C to abort.")
    input("Press Enter to continue...")

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return 1
    email = input("Enter your email: ")
    try:
        admin = Users(username=username,email=email, verified=True, is_admin=True, date_verified=datetime.utcnow())
        admin.generate_password_hash(password)
        db.session.add(admin)
        db.session.commit()
    except Exception as e:
        print(f"Error creating admin user: {e}")
    print(f"Admin user {username} created successfully.")


if __name__ == "__main__":
    cli()
    
    
    # what data type do i store password column on my postgres database 