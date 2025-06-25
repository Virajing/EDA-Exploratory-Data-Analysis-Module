import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("Titanic")

print(df.info())
print(df.describe())
print("Before ", df.isnull().sum())

df["age"].fillna(df["age"].mean(), inplace=True)
df.dropna(subset=["embarked"], inplace=True)

print("After: ", df.isnull().sum())

def createSurvivalChart():
    sns.countplot(x="survived", data=df)
    plt.title("Survival Chart")
    plt.show()

def createSurvivalClass():
    sns.countplot(x="pclass", hue="survived", data=df)
    plt.title("Survival chart by class")
    plt.show()

def createSurvivalGender():
    sns.countplot(x="sex", hue="survived", data=df)
    plt.title("survival chart by gender")
    plt.show()

createSurvivalChart()
createSurvivalClass()
createSurvivalGender()


