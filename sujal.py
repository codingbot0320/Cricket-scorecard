#splesh screen

from tkinter import *
from tkinter.ttk import Progressbar
import time


def splesh():
    w = Tk()
    w.geometry("800x533+200+100")
    w.overrideredirect(True)

    canvas = Canvas(w, width=800, height=533)
    canvas.pack()
    
     # Load an image with a transparent background
    bg_image = PhotoImage(file="cricket.png")
    canvas.create_image(0, 0, anchor='nw', image=bg_image)
   

    # Create a rectangle on the canvas for text background (simulating transparency)
    #text_bg = canvas.create_rectangle(220, 0, 600, 60, fill='white', outline='')
    
    # Add text on top of the text background (within the rectangle)
    text = canvas.create_text(60, 10, text="SCOREBUZZ", font=('Times', 40, 'bold', 'italic'), anchor='nw', fill='Black')
  

    text = canvas.create_text(650,500, text="Version - 2.0.01", font=('Times', 15, 'bold'), anchor='nw', fill='Black')

    progress = Progressbar(w, orient = HORIZONTAL,length = 350)
    progress.place(x=200,y=454)


    text1 = canvas.create_text(555,454, text="0%", font=('Arial', 16, 'bold'), anchor='nw', fill='Black')
    lbl2 = Label(w,text="LOADING",font=("times",20,'bold'))
    lbl2.place(x=300,y=480)

    lbl3 = Label(w,text="",font=("times",20,'bold'))
    lbl3.place(x=300,y=480)

    lbl4 = Label(w,text="",font=("times",20,'bold'))
    lbl4.place(x=300,y=480)

    lbl5 = Label(w,text="",font=("times",20,'bold'))
    lbl5.place(x=300,y=480)

    lbl6 = Label(w,text="Made by ~~Sujal Fuldevare",font=("Verdana",10))
    lbl6.place(x=0,y=580)

    def bar(): 

            for i in range(1,101,):
                    progress['value'] = i
                    w.update_idletasks() 
                    time.sleep(0.03)
                    s=str(i)+" %"
                    p="INITIALIZING"
                    d="Checking OS        "
                    f="Unzipping          "
            
                    canvas.itemconfig(text1, text=s)
                    if i == 20:
                        lbl2.destroy()
                        lbl3.config(text= p)
                    elif i == 50:
                        lbl3.destroy()
                        lbl4.config(text= d)
                
                    elif i == 70:
                        lbl4.destroy()
                        lbl5.config(text= f)
                 
    def close():
        bar()
        w.destroy()
        
    w.after(1,close)


    w.mainloop()

    def show():
        import sujal

    show()



if __name__ == '__main__':
    splesh()
else:
    print("Error : Code 101")
 
 
 
import requests
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class CricketScorecard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cricket Scorecard")
        self.geometry("870x650+200+100")  # Set the window size
        algerian = Font(family="Algerian", size=20, weight="bold")
        self.resizable(False,False)
        
      
        

        self.runs_team_a = 0
        self.runs_team_b = 0
        self.wickets_team_a = 0
        self.wickets_team_b = 0
        self.balls_team_a = 0  # New variable to store balls played for Team A
        self.balls_team_b = 0  # New variable to store balls played for Team B

        # Variables to store batsman and bowler names
        self.batsman_team_a = tk.StringVar()
        self.bowler_team_a = tk.StringVar()
        self.batsman_team_b = tk.StringVar()
        self.bowler_team_b = tk.StringVar()

        # Font for bold labels
        bold_font = Font(weight="bold")

        # Heading
        heading_label = ttk.Label(self, text="Cricket Scorecard", font=algerian, padding=(0, 10))
        heading_label.grid(row=0, column=0, columnspan=10)
        heading_label.configure(foreground="Blue")

        # Labels for Team A - Runs
        ttk.Label(self, text="Team A", font=algerian).grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self, text="Runs:", font=algerian).grid(row=2, column=0, padx=10, pady=10)
        self.runs_label_team_a = ttk.Label(self, text=str(self.runs_team_a), font=bold_font)
        self.runs_label_team_a.grid(row=2, column=1, padx=10, pady=10)

        # Labels for Team A - Wickets
        ttk.Label(self, text="Wickets:", font=algerian).grid(row=3, column=0, padx=10, pady=10)
        self.wickets_label_team_a = ttk.Label(self, text=str(self.wickets_team_a), font=bold_font)
        self.wickets_label_team_a.grid(row=3, column=1, padx=10, pady=10)

        # Labels for Team A - Balls
        ttk.Label(self, text="Balls:", font=algerian).grid(row=4, column=0, padx=10, pady=10)
        self.balls_label_team_a = ttk.Label(self, text=str(self.balls_team_a), font=bold_font)
        self.balls_label_team_a.grid(row=4, column=1, padx=10, pady=10)

        # Entry widgets for Batsman and Bowler names - Team A
        ttk.Label(self, text="Batsman:", font=algerian).grid(row=5, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.batsman_team_a).grid(row=5, column=1, padx=10, pady=10)

        ttk.Label(self, text="Bowler:", font=algerian).grid(row=6, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.bowler_team_a).grid(row=6, column=1, padx=10, pady=10)

        # Labels for Team B - Runs
        ttk.Label(self, text="Team B", font=algerian).grid(row=1, column=3, padx=10, pady=10)
        ttk.Label(self, text="Runs:", font=algerian).grid(row=2, column=3, padx=10, pady=10)
        self.runs_label_team_b = ttk.Label(self, text=str(self.runs_team_b), font=bold_font)
        self.runs_label_team_b.grid(row=2, column=4, padx=10, pady=10)

        # Labels for Team B - Wickets
        ttk.Label(self, text="Wickets:", font=algerian).grid(row=3, column=3, padx=10, pady=10)
        self.wickets_label_team_b = ttk.Label(self, text=str(self.wickets_team_b), font=bold_font)
        self.wickets_label_team_b.grid(row=3, column=4, padx=10, pady=10)

        # Labels for Team B - Balls
        ttk.Label(self, text="Balls:", font=algerian).grid(row=4, column=3, padx=10, pady=10)
        self.balls_label_team_b = ttk.Label(self, text=str(self.balls_team_b), font=bold_font)
        self.balls_label_team_b.grid(row=4, column=4, padx=10, pady=10)

        # Entry widgets for Batsman and Bowler names - Team B
        ttk.Label(self, text="Batsman:", font=algerian).grid(row=5, column=3, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.batsman_team_b).grid(row=5, column=4, padx=10, pady=10)

        ttk.Label(self, text="Bowler:", font=algerian).grid(row=6, column=3, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.bowler_team_b).grid(row=6, column=4, padx=10, pady=10)

        # Buttons
       
      # Buttons
        ttk.Button(self, text="Team A Run 0", command=lambda: self.update_score(0, team='A')).grid(row=7, column=0, pady=10, padx=0)
        ttk.Button(self, text="Team A Run 1", command=lambda: self.update_score(1, team='A')).grid(row=7, column=1, pady=10, padx=0)
        ttk.Button(self, text="Team A Run 2", command=lambda: self.update_score(2, team='A')).grid(row=7, column=2, pady=10, padx=0)
        ttk.Button(self, text="Team A Run 3", command=lambda: self.update_score(3, team='A')).grid(row=7, column=3, pady=10, padx=0)
        ttk.Button(self, text="Team A Run 4", command=lambda: self.update_score(4, team='A')).grid(row=7, column=4, pady=10, padx=0)
        ttk.Button(self, text="Team A Run 6", command=lambda: self.update_score(6, team='A')).grid(row=7, column=5, pady=10, padx=0)
        ttk.Button(self, text="Team A Wicket", command=lambda: self.update_wickets(team='A')).grid(row=8, column=0, pady=10 ,padx=0)
        ttk.Button(self, text="Team A No Ball", command=lambda: self.no_ball(team='A')).grid(row=8, column=1, pady=10, padx=0)
        ttk.Button(self, text="Team A Wide", command=lambda: self.wide(team='A')).grid(row=8, column=2, pady=10, padx=0)

        ttk.Button(self, text="Team B Run 0", command=lambda: self.update_score(0, team='B')).grid(row=9, column=0, pady=10, padx=0)
        ttk.Button(self, text="Team B Run 1", command=lambda: self.update_score(1, team='B')).grid(row=9, column=1, pady=10, padx=0)
        ttk.Button(self, text="Team B Run 2", command=lambda: self.update_score(2, team='B')).grid(row=9, column=2, pady=10, padx=0)
        ttk.Button(self, text="Team B Run 3", command=lambda: self.update_score(3, team='B')).grid(row=9, column=3, pady=10, padx=0)
        ttk.Button(self, text="Team B Run 4", command=lambda: self.update_score(4, team='B')).grid(row=9, column=4, pady=10, padx=0)
        ttk.Button(self, text="Team B Run 6", command=lambda: self.update_score(6, team='B')).grid(row=9, column=5, pady=10, padx=0)
        ttk.Button(self, text="Team B Wicket", command=lambda: self.update_wickets(team='B')).grid(row=10, column=0, pady=10, padx=0)
        ttk.Button(self, text="Team B No Ball", command=lambda: self.no_ball(team='B')).grid(row=10, column=1, pady=10, padx=0)
        ttk.Button(self, text="Team B Wide", command=lambda: self.wide(team='B')).grid(row=10, column=2, pady=10, padx=0)


        # End match button
        ttk.Button(self, text="End Match", command=self.display_scorecard).grid(row=13, column=0, columnspan=7, pady=10)

    def update_score(self, runs, team):
        # Increment runs and balls based on the button clicked and the team specified
        if team == 'A':
            self.runs_team_a += runs
            self.balls_team_a += 1
            self.runs_label_team_a.config(text=str(self.runs_team_a))
            self.balls_label_team_a.config(text=str(self.balls_team_a))
        elif team == 'B':
            self.runs_team_b += runs
            self.balls_team_b += 1
            self.runs_label_team_b.config(text=str(self.runs_team_b))
            self.balls_label_team_b.config(text=str(self.balls_team_b))
            
    def no_ball(self, team):
        if team == 'A':
            self.runs_team_a += 1
            self.runs_label_team_a.config(text=str(self.runs_team_a))
        elif team == 'B':
            self.runs_team_b += 1
            self.runs_label_team_b.config(text=str(self.runs_team_b))
            
    def wide(self, team):
        if team == 'A':
            self.runs_team_a += 1
            self.runs_label_team_a.config(text=str(self.runs_team_a))
        elif team == 'B':
            self.runs_team_b += 1
            self.runs_label_team_b.config(text=str(self.runs_team_b))

    def update_wickets(self, team):
        # Increment wickets and balls based on the button clicked and the team specified
        if team == 'A':
            self.wickets_team_a += 1
            self.wickets_label_team_a.config(text=str(self.wickets_team_a))
            self.balls_team_a += 1  # Increment balls after a wicket
            self.balls_label_team_a.config(text=str(self.balls_team_a))
        elif team == 'B':
            self.wickets_team_b += 1
            self.wickets_label_team_b.config(text=str(self.wickets_team_b))
            self.balls_team_b += 1  # Increment balls after a wicket
            self.balls_label_team_b.config(text=str(self.balls_team_b))
            
    def calculate_strike_rate(self, runs, balls):
        strike_rate = (runs / balls) * 100 if balls > 0 else 0
        return round(strike_rate, 2)
    def calculate_average(self, runs, wickets):
        average = runs / wickets if wickets > 0 else runs
        return round(average, 2)
    

    def display_scorecard(self):
        # Create a new window for the scorecard
        scorecard_window = tk.Toplevel(self)
        scorecard_window.title("Match Summary")
        scorecard_window.geometry("800x500")
        
         # Get the names entered for both teams from the entry fields
        name_team_a = self.batsman_team_a.get()
        name_team_b = self.batsman_team_b.get()
            
             # Display the final scores, wickets, balls, and player names for both teams
        ttk.Label(scorecard_window, text=f"{name_team_a} Score:",font=('bold',20)).grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.runs_team_a),font=('bold',20)).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(scorecard_window, text=f"{name_team_a} Wickets:",font=('bold',20)).grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.wickets_team_a),font=('bold',20)).grid(row=1, column=1, padx=10, pady=5)
        ttk.Label(scorecard_window, text=f"{name_team_a} Balls:",font=('bold',20)).grid(row=1, column=2, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.balls_team_a),font=('bold',20)).grid(row=1, column=3, padx=10, pady=5)

        ttk.Label(scorecard_window, text=f"{name_team_b} Score:",font=('bold',20)).grid(row=2, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.runs_team_b),font=('bold',20)).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(scorecard_window, text=f"{name_team_b} Wickets:",font=('bold',20)).grid(row=3, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.wickets_team_b),font=('bold',20)).grid(row=3, column=1, padx=10, pady=5)
        ttk.Label(scorecard_window, text=f"{name_team_b} Balls:",font=('bold',20)).grid(row=3, column=2, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.balls_team_b),font=('bold',20)).grid(row=3, column=3, padx=10, pady=5)

        # Calculate and display the highest scorer and highest wicket-taker
        name_highest_scorer = name_team_a if self.runs_team_a > self.runs_team_b else name_team_b
        ttk.Label(scorecard_window, text="Highest Scorer:",font=('bold',20)).grid(row=4, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=name_highest_scorer,font=('bold',20)).grid(row=4, column=1, padx=10, pady=5)

        name_highest_wicket_taker = name_team_a if self.wickets_team_a > self.wickets_team_b else name_team_b
        ttk.Label(scorecard_window, text="Highest Wicket-Taker:",font=('bold',20)).grid(row=5, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=name_highest_wicket_taker,font=('bold',20)).grid(row=5, column=1, padx=10, pady=5)


        ttk.Label(scorecard_window, text="Team A Batsman Strike Rate:",font=('bold',20)).grid(row=7, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.calculate_strike_rate(self.runs_team_a, self.balls_team_a)),font=('bold',20)).grid(row=7, column=1, padx=10, pady=5)

        ttk.Label(scorecard_window, text="Team B Batsman Strike Rate:",font=('bold',20)).grid(row=8, column=0, padx=10, pady=5)
        ttk.Label(scorecard_window, text=str(self.calculate_strike_rate(self.runs_team_b, self.balls_team_b)),font=('bold',20)).grid(row=8, column=1, padx=10, pady=5)
        
    
           
if __name__ == "__main__":
    CricketScorecard().mainloop()
