import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")
#print(list(df.columns))

# Make 2 data frames for female and male passengers
dfMale = df[df["Sex"] == 'male']
dfFem = df[df["Sex"] == 'female']

#fig,ax = plt.figure(figsize = (10,5))
fig,ax = plt.subplots(2,2,figsize = (10,5))
ax[0,0].scatter(dfMale["Age"],dfMale["SibSp"])
ax[0,0].set_title("Male SibSp")
ax[0,0].set_xlabel("Age")
ax[0,0].set_ylabel("Number of Siblings/Spouses")
ax[0,0].set_xlim([0,100])
ax[0,0].set_yticks(range(0,6,1))

ax[0,1].scatter(dfFem["Age"],dfFem["SibSp"])
ax[0,1].set_title("Female SibSp")
ax[0,1].set_xlabel("Age")
ax[0,1].set_ylabel("Number of Siblings/Spouses")
ax[0,1].set_xlim([0,100])
ax[0,1].set_yticks(range(0,6,1))

ax[1,0].scatter(dfMale["Age"],dfMale["Parch"])
ax[1,0].set_title("Male Parch")
ax[1,0].set_xlabel("Age")
ax[1,0].set_ylabel("Number of Parents/Children")
ax[1,0].set_xlim([0,100])
ax[1,0].set_yticks(range(0,7,2))

ax[1,1].scatter(dfFem["Age"],dfFem["Parch"])
ax[1,1].set_title("Female Parch")
ax[1,1].set_xlabel("Age")
ax[1,1].set_ylabel("Number of Parents/Children")
ax[1,1].set_xlim([0,100])
ax[1,1].set_yticks(range(0,7,2))


plt.subplots_adjust(hspace = 0.8)
plt.show()

