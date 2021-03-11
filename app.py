from flask import Flask, render_template, request, redirect, url_for
from forms import Todo

# BOWLING GAME: START
# RUN PYTHON3 app.py on Terminal

app = Flask(__name__)

class BowlingGame:
    def __init__(self):
        self.rolls = []
        
    def single_roll(self, pins):
        self.rolls.append(pins)
  
    def score(self):
        total_score = 0
        roll_idx = 0
        for i in range(0,10):
            if(self.isStrike(roll_idx)):
                if(self.rolls[roll_idx+2] == '/'):
                    total_score += 10 + 10
                    roll_idx += 1
                
                else:
                    total_score += 10 + self.convert_scores(self.rolls[roll_idx+1],roll_idx+1) + self.convert_scores(self.rolls[roll_idx+2],roll_idx+2)
                    roll_idx += 1
                
            elif(self.isSpare(roll_idx)):
                total_score += 10 + self.convert_scores(self.rolls[roll_idx+2],roll_idx+2)
                roll_idx += 2
            
            else:
                total_score += self.convert_scores(self.rolls[roll_idx],roll_idx)+self.convert_scores(self.rolls[roll_idx+1],roll_idx+1)
                roll_idx += 2
        
        print(total_score)
        return total_score
        

    def convert_scores(self,roll,roll_idx):
        rolls = self.rolls
        if roll == "X":
            return 10
            
        #spare 
        elif roll == "/": 
            try:
                num = 10 - (int(rolls[roll_idx-1]))
            except ValueError:
                num = 10 - 0
            return num
        
        elif roll == "-":
            return 0
        
        else:
            # change to num
            return int(roll)


    def isStrike(self,roll_idx):
        return self.convert_scores(self.rolls[roll_idx],roll_idx) == 10
           
        
        
    def isSpare(self,roll_idx):
        if self.convert_scores(self.rolls[roll_idx],roll_idx)+ self.convert_scores(self.rolls[roll_idx + 1],roll_idx+1) == 10:
            return True


@app.route('/', methods=['GET', 'POST'])
def index(): 
    request_method = request.method
    if request.method =='POST':
        name = request.form['name']
        return redirect(url_for('findscore', name=name))
    return render_template('main.html',request_method=request_method)

@app.route("/findscore/<string:name>", methods=['GET', 'POST'])
def findscore(name):
    return render_template('findscore.html',name=name)

@app.route('/getscore',methods = ['POST', 'GET'])
def result():
    game = BowlingGame()
    score1s = []
    score2s = []
    scores = []
    if request.method == 'POST':
        for key, value in request.form.items():
            if "-first" in key:
                score1s.append(value)
            if "-second" in key:
                score2s.append(value)
        for i in range (0,10):
            scores.append(score1s[i])
            scores.append(score2s[i])

        for pins in range (0,len(scores)):
            game.single_roll(scores[pins])
    
        totalscore = game.score()
            
            
            # print("key: {0}, value: {1}".format(key, value))
        # result = request.form
        return render_template("getscore.html", result=totalscore)




app.run(host='0.0.0.0', port=81, debug=True)