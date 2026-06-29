from PlayerStats import Player
from StatsCalculator import Stats

from flask import Flask, render_template,request

app = Flask(__name__)

players = {}

def safe_int(value):
    try:
        return int(value) 
    
    except ValueError:
        return 0


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_players', methods = ['GET', 'POST'])
def addplayers():


    if request.method == 'POST':
        name = request.form['name']
        points = safe_int(request.form['points'])
        rebounds = safe_int(request.form['rebounds'])
        assists = safe_int(request.form['assists'])
        blocks = safe_int(request.form['blocks'])
        steals = safe_int(request.form['steals'])
        games_played = safe_int(request.form['games'])
    
    
        player = Player(name, points, rebounds, assists, blocks, steals, games_played)
        
        players[player.name] = player

        return render_template("addplayer.html", player_added = player)
    return render_template("addplayer.html")

@app.route('/view_players')
def ViewPlayers():
    return render_template("players.html", players= players)


if __name__ == "__main__":
    app.run(debug=True)