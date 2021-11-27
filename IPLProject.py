'''Project: IPL 2020 Player Analysis
By- Achintya Gupta(XII-S1)
    Aditya Pathak(XII-B)
    Dhruv Chopra(XII-S1)
    Dashmesh Singh Chehal(XII-H)'''

#modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#CSV files/ Dataframes
bat=pd.read_csv("batsmen.csv")
bowl=pd.read_csv("bowlers.csv")
allr=pd.read_csv("allrounders.csv")
plyr=pd.concat([bat,bowl,allr], ignore_index=True)

#Defined functions
def max1(dataF, val2, N):
    df=dataF.sort_values(by=[val2], ascending=False)
    print(df[["Name_Of_Player", val2]].head(N))
    L1=df["Name_Of_Player"].head(N)
    L2=df[val2].head(N)
    plt.scatter(L2, L1, c=np.random.rand(N), marker='h',s=300)
    plt.show()

def minim1(dataF, val2, N):
    df=dataF.sort_values(by=[val2])
    print(df[["Name_Of_Player", val2]].head(N))
    L1=df["Name_Of_Player"].head(N)
    L2=df[val2].head(N)
    plt.plot(L2, L1, marker='h', color='k', markersize=10)
    plt.show()
    
def avg1(dataF, val2):
    L1=dataF.groupby("Team")[val2].mean()
    print(L1)
    dataF.groupby("Team")[val2].mean().plot(marker='h', c='red', markersize=10)
    plt.show()

def max2(dataF, val2):
     print(dataF.groupby("Team")[val2].max())
     dataF.groupby("Team")[val2].max().plot(marker='h', c='green', markersize=10)
     plt.show()
     
def min2(dataF, val2):
      print(dataF.groupby("Team")[val2].min())
      dataF.groupby("Team")[val2].min().plot(marker='h', c='yellow', markersize=10)
      plt.show()
      
def asc(dataF, val2):
    df=dataF.sort_values(by=[val2])
    print(df[["Name_Of_Player", val2]])
    
def desc(dataF, val2):
    df=dataF.sort_values(by=[val2], ascending=False)
    print(df[["Name_Of_Player", val2]])

def cnt3(dataF,val2):
    print(dataF.groupby(val2)[val2].count())
    dataF.groupby(val2)[val2].count().plot(kind='bar', color='aqua')
    plt.show()
    
#Menu
val2='.'
while val2!='E':
    print("Choose category of player:")
    print("1. Batsman \n2. Bowler \n3. All-rounder \n4. All players \n5. Exit Programme" )
    val1=int(input("Enter 1, 2, 3, 4 or 5: "))
    if val1==5:
        val2='E'
        break
    

#Batsman
    if val1==1:
        DF= bat
        print("Choose category of analysis: ")
        for i in bat:
            if i!= "Name_Of_Player":
                print(i)
        print("Press 'R' to return to main menu, 'E' to exit")
        val2=input("Enter choice: ")
        if val2=='R':
            continue
        elif val2=='E':
            break

#Bowler
    elif val1==2:
        DF= bowl
        print("Choose category of analysis: ")
        for i in bowl:
            if i!= "Name_Of_Player":
                print(i)
        print("Press 'R' to return to main menu, 'E' to exit")
        val2=input("Enter choice: ")
        if val2=='R':
            continue
        elif val2=='E':
            break
   
#All-rounder
    elif val1==3:
        DF= allr
        print("Choose category of analysis: ")
        for i in allr:
            if i!= "Name_Of_Player":
                print(i)
        print("Press 'R' to return to main menu, 'E' to exit")
        val2=input("Enter choice: ")
        if val2=='R':
            continue
        elif val2=='E':
            break
#All players
    elif val1==4:
        DF= plyr
        print("Choose category of analysis: ")
        for i in plyr:
            if i!= "Name_Of_Player":
                print(i)
        print("Press 'R' to return to main menu, 'E' to exit")
        val2=input("Enter choice: ")
        if val2=='R':
            continue
        elif val2=='E':
            break
    Num= ['100s', '4s', '50s','5w','6s','BBM', 'Ball_SR', 'Balls_Bowld', 'Bat_Avg', 'Bat_SR','Bowl_Avg', 'Eco', 'Highest_Score', 'Innings_Batted', 'Innings_Bowled', 'Matches', 'Runs_Conceded', 'Runs_Scored', 'Wickets']
    if val2 in Num:
        print("Choose type of analysis")
        print("1. Maximum N players \n2. Minimum N players \n3. Average per team \n4. Maximum by team(Only Value) \n5. Minimum per team(Only Value) \n6. Ascending order \n7. Descending order \n8. Return to Main Menu")
        val4=int(input("Enter Choice no.: "))
    
        if val4== 1:
            N= int(input("Enter value of N: "))
            max1(DF, val2, N)
        if val4== 2:
            N= int(input("Enter value of N: "))
            minim1(DF, val2, N)
        if val4== 3:
            avg1(DF, val2)
        if val4== 4:
            max2(DF, val2)
        if val4== 5:
            min2(DF, val2)
        if val4== 6:
            asc(DF, val2)
        if val4== 7:
            desc(DF, val2)
        
        elif val4==8:
            continue
    if val2 not in Num:
        cnt3(DF, val2)
    val2=input("Press Enter key to continue, Write 'E'to Exit: ")
        
    
if val2=='E':
    print("Thank you for using our programme")