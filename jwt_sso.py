from flask import Flask,request,redirect,render_template
import encoding_decoding

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def jwt_generation():
    client_id = request.args.get('client_id')
    state = request.args.get('state')
    redirect_uri = request.args.get('redirect_uri')
    nonce = request.args.get('nonce')
    #return '''{}'''.format(state)
    token=encoding_decoding.jwt_token(nonce)
    constructed_url = redirect_uri+'?state='+state+'&id_token='+token
    return redirect(constructed_url,code=302)

# @app.route('/login_page',methods=['GET'])
# def login():
#   return  render_template('login.html')