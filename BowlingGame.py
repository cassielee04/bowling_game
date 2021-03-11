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
