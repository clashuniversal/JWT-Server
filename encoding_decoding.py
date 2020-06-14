import jwt
from datetime import datetime
def jwt_token(nonce):
    private_key = open('jwtRS256.key').read()
    payload = {'sub': 'ue839','email':'jwttest@freshworks.com','iat': datetime.utcnow(),'nonce': nonce,'first_name': 'Test','given_name':'JWT'}
    headers = { "alg": "RS256", "typ": "JWT"}
    token = jwt.encode(payload,private_key,algorithm='RS256',headers=headers).decode('utf=-8')
    #print(token)
    public_key = open('jwtRS256.key.pub').read()
    decoded_payload = jwt.decode(token,public_key,algorithms='RS256')
    #print(decoded_payload)
    return token

#print(type(jwt_token('This is new Nonce')))
