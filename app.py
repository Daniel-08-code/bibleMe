import sqlite3
from flask import Flask,render_template,request,redirect,jsonify


class Utilisateur:
    def __init__(self,email,nom,age,pays,motDePasse):
        self.email = email
        self.nom = nom
        self.age = age
        self.pays = pays
        self.motDePasse = motDePasse
    def jouerPartie(self):
        partie = Partie()
        return partie 
    
class Partie:
    score = 0
    vie = 3
    def incrementerScore(self):
        self.score = self.score+1
        
    def decrementerVie(self):
        self.vie = self.vie-1
    
    def finirPartie(self):
        if self.vie == 0:
            return f"La partie est terminee !... votre score est : {self.score}"
    


app = Flask(__name__)

app.static_folder = 'static'
app.template_folder = 'templates'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    partie1 = Partie()

    conn = sqlite3.connect('database.db')
    cur = conn.cursor() 
    cur.execute("SELECT * FROM questionsReponses ORDER BY RANDOM() LIMIT 1")
    resultat = cur.fetchone()
        
    conn.commit()
    conn.close()
            
        
    return render_template('quiz.html',resultat=resultat,partie1 = partie1)

@app.route('/changerQuestion')
def changerQuestion():

    conn = sqlite3.connect('database.db')
    cur = conn.cursor() 
    cur.execute("SELECT * FROM questionsReponses ORDER BY RANDOM() LIMIT 1")
    resultat = cur.fetchone()
        
    conn.commit()
    conn.close()
            
        
    return jsonify(resultat)


@app.route('/score')
def show_score():
    # Récupérer le score depuis la requête
    score = request.args.get('score')

    # Rendre le template score.html en passant le score récupéré
    return render_template('score.html', score=score)
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
