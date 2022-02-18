class Login:
    def __init__(self, token):
        self.token = token
    def get_token_details(self):
        print("Le token est : {}".format(self.token))