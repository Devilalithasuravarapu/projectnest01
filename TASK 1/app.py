from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key
socketio = SocketIO(app)

# A dictionary to store poll data (in-memory storage, you may use a database in production)
poll_data = {'option_A': 0, 'option_B': 0}

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/vote')
def vote():
    return render_template('vote.html')

@socketio.on('vote')
def handle_vote(vote_data):
    # Process the vote data (e.g., update the poll_data dictionary)
    option = vote_data['option']
    poll_data[option] += 1

    # Emit the updated results to all connected clients
    emit('update_results', poll_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)