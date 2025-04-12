"""
If you are planning on going out to see a movie, how well can you trust online reviews and ratings? *Especially*
if the same company showing the rating *also* makes money by selling movie tickets. Do they have a bias towards rating movies higher than 
they should be rated?
"""
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

fandango = pd.read_csv("fandango_scrape.csv")
#print(fandango.head())
print()
#print(fandango.describe())

def fandogo_score():
    """
    **1)TASK: Let's explore the relationship between popularity of a film and its rating.
      Create a scatterplot showing the relationship between rating and votes. Feel free to edit visual styling to your preference.**
      2)**TASK: Calculate the correlation between the columns:**
    """
    plt.figure(figsize=(10,4),dpi=200)
    sns.scatterplot(data=fandango,x='RATING',y='VOTES')
    plt.show()
    print(fandango.corr())
def movies_per_year():
    #**TASK: Visualize the count of movies per year with a plot:**

    fandango['Year']=fandango['FILM'].apply(lambda title:title.split('(')[-1].replace(')','')) # to convert film format of title(Year)
    #print(fandango['Year']) into Separate Year column 
    plt.figure(figsize=(10,4),dpi=200)
    sns.countplot(data=fandango,x='Year')
    plt.show()
def rating_visualization():
    """
    sns.kdeplot(data=fan_review,x='RATING',fill=True,clip=(0,5),label='True Rating')
    sns.kdeplot(data=fan_review,x='STARS',fill=True,clip=(0,5),label='Star Displayed')
    plt.legend()
    plt.show()
    """
    fan_review=fandango[fandango['VOTES']>0]
    fan_review['Star_Diff']=fan_review['STARS']-fan_review['RATING']
    fan_review['Star_Diff']=fan_review['Star_Diff'].round(2)
    sns.countplot(data=fan_review,x='Star_Diff',palette='magma')
    plt.show()





#movies_per_year()
#fandogo_score()
rating_visualization()