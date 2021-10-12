#gymnastics_scoring_functions.py
#calculate average gymnastics scores with user input
#last edited by Sarah Giskin 10/14/19

#define functions
def score_function():
    print("Score for Judge", judge_count + 1, "is", judge_score, ".")
    return judge_score


def average_function():
    score_average = round((score_sum / judge_count), 2)
    print("The average score is", score_average, ".")
    return score_average


#main program


#assign variables
judge_count = 0 
score_sum = 0.0


#create count controlled loop
while judge_count < 6:
    judge_score = float(input("Enter judge's score: "))
    print (score_function())


    #update variables
    judge_count = judge_count + 1
    score_sum = score_sum + judge_score


#print average score
average_function()

