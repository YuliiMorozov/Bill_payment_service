from indication import db
from indication.models import User

def create_admin_user():

    check_admin = (
        db.session
        .query(User)
        .filter_by(is_admin=True)
        .first()
    )

    if check_admin:
        print("YES")
    else:
        print("NO")