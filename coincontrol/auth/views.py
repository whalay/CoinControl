from coincontrol.auth import auth


@auth.route('/register', methods=["POST"])
def register():
    pass

@auth.route('/login', methods=["POST"])
def login():
    pass

@auth.route('/logout', methods=["POST"])
def logout():
    pass