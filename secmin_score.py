marksheet = []#add names and marks
scoresheet = []#for getting marks
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scoresheet+=[score]
    #print(marksheet)
    #print((sorted(set(scoresheet)))[1])#second least number
    sec_min_score= sorted(set(scoresheet))[1]
    #print(sorted(marksheet))--> here sorting takes place by name
    

    for name,score in sorted(marksheet):
        if(score==sec_min_score):
               print(name)
       
  
        

