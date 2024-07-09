from flask import Flask ,render_template
from flask_socket import socketIO, send


#Creat fask instance
app = Flask(__name__)

#set sectret key for session management
app.config['SECRET_KEY'] = '+++5657'

#initialize socketIO with the flask app
socketio = socketIO(app)

#define route
@app.route('/')
def index():
    return render_template('index.html')


socketio.on('message')
def handle_message(msg):
    print(f'message:{msg}')
    send(msg,broadcast=True)


if __name__ == '__main__':
    socketio.run(app,debug=True)
