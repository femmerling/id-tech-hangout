import json

from authpy.auth.ttypes import TokenNotValidException
from authpy.auth.ttypes import UserAlreadyExistException


class AuthHandler(object):

    def authenticate(self, access_token):
        if access_token == 'id-tech':
            return json.dumps(
                    {
                        'user': 'id-tech',
                        'email': 'id-tech@id-tech.com'
                    }
            )
        else:
            raise TokenNotValidException(
                error_code=403,
                message='this access token is not valid')

    def register_client(self, name, email):
        existed = False
        users = self.get_user_data()
        for user in users:
            if user['name'] == name and user["email"] == email:
                existed = True
        if existed:
            raise UserAlreadyExistException(
                    error_code=409,
                    message='this user already existed'
            )

        new_user = json.dumps({'name': name, 'email': email})
        self.append_user(new_user)
        return new_user

    def append_user(self, user_string):
        with open('users.txt', 'a') as user_file:
            user_file.write("%s\n" % user_string)

    def get_user_data(self):
        content = []
        with open('users.txt') as user_file:
            content = user_file.readlines()
        content = [json.loads(user) for user in content]
        return content
