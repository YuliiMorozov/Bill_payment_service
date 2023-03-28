from indication.models.user import User
from indication import db

def add_admin():

    check_admin = (
        db.session
        .query(User)
        .filter_by(username='admin_user')
        .first()
    )

    if check_admin is None:

        admin_user = User(
            username = "admin_user",
            email = "admin_user@gmail.com",
            is_admin = True
            )
        admin_user.set_password("admin_user")

        db.session.add(admin_user)
        db.session.commit()