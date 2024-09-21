from users.repository import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def create_user(username, email):
        return UserRepository.create_user(username, email)

    @staticmethod
    def update_user(user_id, username, email):
        return UserRepository.update_user(user_id, username, email)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)

    @staticmethod
    def serialize_user(user):
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }