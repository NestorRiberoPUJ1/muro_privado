from flask_app.config.mysqlconnection import connectToMySQL


class Message:

    def __init__(self, data: dict):
        self.id = data["id"]
        self.content = data["content"]
        self.sender_id = data["sender_id"]
        self.receiver_id = data["receiver_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.sender = data["sender"]
        self.receiver = data["receiver"]

    @classmethod
    def save(cls, form: dict):
        query = "INSERT INTO muro_privado.messages (content, sender_id, receiver_id) VALUES (%(content)s,%(sender_id)s,%(receiver_id)s)"
        result = connectToMySQL("muro_privado").query_db(query, form)
        return result

    @classmethod
    def delete(cls, form: dict):
        query = "DELETE FROM muro_privado.messages WHERE messages.id= %(id)s"
        result = connectToMySQL("muro_privado").query_db(query, form)
        return result

    @classmethod
    def get_user_messages(cls, data):
        query = "SELECT messages.*, users.first_name as sender, users2.first_name as receiver FROM users "\
            "LEFT JOIN messages ON users.id = messages.sender_id " \
            "LEFT JOIN users as users2 ON messages.receiver_id = users2.id " \
            "WHERE receiver_id= %(id)s;"
        results = connectToMySQL("muro_privado").query_db(query, data)
        messages = []
        for x in results:
            messages.append(cls(x))
        return messages
