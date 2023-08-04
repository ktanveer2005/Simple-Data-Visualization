import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load data from CSV files
summary = pd.read_csv("summary.csv")
detail = pd.read_csv("details.csv")
batting = pd.read_csv("batting_card.csv")
bowling = pd.read_csv("bowling_card.csv")

while True:
    print("\nWelcome to the ICC T20 Men's World Cup Database")
    print("\nSelect a Data Visualization Option:")
    print("1. Top scoring batsmen")
    print("2. Top 10 Individual scores")
    print("3. Histogram of Runs")
    print("4. Top economical bowler")
    print("5. Total Wickets")
    print("6. Quit")

    user_choice = input("Enter the option number (1-6): ")

    if user_choice == '1':
        # Step 3: Data Visualization - Top scoring batsmen
        top_batsmen = batting.groupby('fullName').agg({'runs': 'sum', 'ballsFaced': 'sum'})
        top_batsmen = top_batsmen.nlargest(10, 'runs')
        plt.figure(figsize=(10, 8))
        plt.barh(top_batsmen.index, top_batsmen['runs'], color='blue')
        for index, value in enumerate(top_batsmen['runs']):
            plt.text(value, index, str(value), color='white', ha='right', va='center', fontsize=7, fontweight='bold')
        plt.xlabel("Runs")
        plt.ylabel("Batsmen")
        plt.title("Top scoring batsmen")
        plt.show()

    elif user_choice == '2':
        # Step 4: Data Visualization - Top 10 Individual scores
        top_individual_scores = batting.nlargest(10, 'runs')[['fullName', 'runs', 'ballsFaced']]
        plt.figure(figsize=(10, 8))
        plt.scatter(top_individual_scores['runs'], top_individual_scores['fullName'])
        for i in range(len(top_individual_scores)):
            plt.text(top_individual_scores['runs'].iloc[i], top_individual_scores['fullName'].iloc[i],
                     str(top_individual_scores['runs'].iloc[i]), color='grey')
        plt.xlabel("Runs")
        plt.ylabel("Batsmen")
        plt.title("Top 10 Individual scores")
        plt.show()

    elif user_choice == '3':
        # Step 5: Data Visualization - Histogram of Runs
        plt.figure(figsize=(10, 8))
        plt.hist(batting['runs'], bins=30)
        plt.xlabel("Runs")
        plt.ylabel("Frequency")
        plt.title("Histogram of Runs")
        plt.show()

    elif user_choice == '4':
        # Step 6: Data Visualization - Top economical bowler
        top_bowlers = bowling.groupby('fullName').agg({'wickets': 'sum', 'economyRate': 'median'})
        top_bowlers = top_bowlers.nsmallest(10, 'economyRate')
        plt.figure(figsize=(10, 8))
        plt.barh(top_bowlers.index, top_bowlers['economyRate'], color='maroon')
        for index, value in enumerate(top_bowlers['economyRate']):
            plt.text(value, index, str(value), color='white', ha='right', va='center', fontsize=7, fontweight='bold')
        plt.xlabel("Median Economy Rate")
        plt.ylabel("Bowler")
        plt.title("Top economical bowler")
        plt.show()

    elif user_choice == '5':
        # Step 7: Data Visualization - Total wickets
        top_wicket_takers = bowling.groupby('fullName').agg({'wickets': 'sum'})
        top_wicket_takers = top_wicket_takers.nlargest(10, 'wickets')
        plt.figure(figsize=(10, 8))
        plt.barh(top_wicket_takers.index, top_wicket_takers['wickets'], color='maroon')
        for index, value in enumerate(top_wicket_takers['wickets']):
            plt.text(value, index, str(value), color='white', ha='right', va='center', fontsize=7, fontweight='bold')
        plt.xlabel("Number of Wickets")
        plt.ylabel("Bowler")
        plt.title("Total Wickets")
        plt.show()

    elif user_choice == '6':
        print("Quitting the program.")
        break

    else:
        print("Invalid option. Please enter a valid option number (1-6).")
