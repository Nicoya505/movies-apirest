from jwt import encode, decode

class JwtManager():

    @classmethod
    def create_token(self, data: dict):
        token: str = encode(payload=data, key="this_is_my_key", algorithm="HS256")
        return token
    

    @classmethod
    def validate_token(self, token: str):
        data: dict = decode(token, key="this_is_my_key", algorithms=["HS256"])
        return data