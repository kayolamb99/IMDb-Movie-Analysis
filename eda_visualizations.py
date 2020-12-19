#Importing necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Reading in newly cleaned data
movies = pd.read_csv('/Users/kayode/Desktop/Side Projects/SP3_Movies/movies_clean.csv')

#Question 1: What's the correlation between budget and gross?

coeff_1 = np.corrcoef(movies["budget"],movies["gross"])
print(coeff_1)

#Visualization
plt.scatter(movies["budget"],np.sqrt(movies["gross"]))
plt.title("Budget Vs. Gross Profit")
plt.xlabel("Budget ($)")
plt.ylabel("Gross ($)")
plt.show()

#Making the gross column square root seems to make this conform to a linear
#relationship

#Question 2: What effect does being in a major studio have on gross profit?
sns.boxplot(data = movies, x = 'isMajor',y='gross', showfliers = False)

#Question 3: How about budget return?
sns.boxplot(data = movies, x = 'isMajor', y = 'budgetReturn', showfliers = False)

#Question 4: Correlation Matrix for all numerical variables

#Creating the correlation matrix object
corrMatrix = movies.loc[:,("year","runtime","score","votes","budget","gross","budgetReturn")].corr()
sns.heatmap(corrMatrix, annot = True, cmap="YlGnBu")
plt.show()

    #Based on the matrix, it appears as though gross and budget have a high correlation
    #Gross and votes also has a high correlation, indicating some type of relationship
        #between audience score and critical reception
    #Score and votes has a 0.4 correlation, which also makes sense
    #Year and budget has a weaker (0.29) correlation, which is less strong of a relationship
    #than I originally thought


#Question 5: Which of the major studios has the highest rating for its films?
sns.boxplot(data = movies.loc[movies["isMajor"] == 1], x = "score", y = "company")

    #Looks like on average, Disney edges out the competition. Warner Bros
    #with the most variability in the entire set


#Question 6: What's the effect of ratings vs. gross
plt.scatter(movies["score"],movies["gross"])
plt.title("Score vs. Gross")
plt.xlabel("Score")
plt.ylabel("Gross ($)")
plt.show()

    #It looks like this variable has an exponential relationship, or at the
    #very least is very right-skewed
    
#Question 7: Which of the major studios have the highest budget return?
sns.boxplot(data = movies.loc[movies["isMajor"] == 1], x = "budgetReturn", y = "company", showfliers = False)

    #All have a pretty similar budget return score hovering between 1 and 2 times
    #Appears as if Disney again has the highest budget return, with Paramount having the 
    #biggest variability and highest budget-returned movie

#Question 8: Is there a realtionship between runtime and gross?
plt.scatter(movies["runtime"],movies["gross"])
plt.title("Runtime vs Gross")
plt.xlabel("Runtime (Mins)")
plt.ylabel("Gross ($)")
plt.show()

#Question 9: What genre of movies generate the greatest budget return?
sns.boxplot(data = movies, x = "budgetReturn", y = "genre", showfliers = False)
    
    #Budget Return for Horror movies is the most variable, which is to be 
    #expected. Sci-Fi seems to generate the highest budget return behind Horror

#Dataset isolating only movies produced by major studios
movies_major = movies.loc[movies["isMajor"] == 1]

#Question 10: What is the frequency of budget return?
plt.hist(movies["budgetReturn"],range = [0,10])
plt.xlabel("Budget Return")
plt.ylabel("Frequency")
plt.title("Budget Return Distribution")
plt.show()


#How is this impacted by major movie studio?
fig, axes = plt.subplots(1, 6, figsize=(10,2.5), dpi=100, sharex=True, sharey=True)
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:pink', 'tab:olive', 'tab:orange']

for i, (ax, company) in enumerate(zip(axes.flatten(), movies_major.company.unique())):
    x = movies_major.loc[movies_major.company==company, 'budgetReturn']
    ax.hist(x, alpha=0.5, bins=100, density=True, stacked=True, label=str(company), color=colors[i], range = [0,10])
    ax.set_title(company, fontsize = 6)

plt.suptitle('Probability Histogram of Budget Returns', y=1.05, size=16)
ax.set_xlim(0, 3); ax.set_ylim(0, 1);
plt.tight_layout();
    
plt.hist(movies_major["budgetReturn"],range = [0,1])
plt.suptitle("Frequency Histogram of Budget Returns")

#Question 11: What impact does a movie's rating have on its gross?
movies_g = movies.loc[movies["rating"] == "G"]
movies_pg = movies.loc[movies["rating"] == "PG"]
movies_pg13 = movies.loc[movies["rating"] == "PG-13"]
movies_r = movies.loc[movies["rating"] == "R"]
movies_reg_rating = pd.concat([movies_g,movies_pg,movies_pg13,movies_r])
sns.boxplot(data = movies_reg_rating, x = "rating", y = "budgetReturn", showfliers = False)
plt.show()





