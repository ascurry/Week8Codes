import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")
#print(list(df.columns))

# Make 2 data frames for female and male passengers
dfMale = df[df["Sex"] == 'male']
# remove rows in dfMale if NA value in Age column
dfMale = dfMale.dropna(subset=["Age"]) #,inplace = True)
dfMale = dfMale.reset_index(drop=True)

# repeat for Female
dfFem = df[df["Sex"] == 'female']
dfFem = dfFem[pd.notnull(dfFem["Age"])]

# make starting age criteria will use in binning :
StartAge = 0
EndAge = 10

#initialize
MaleAgeDat = []
FemAgeDat = []
X_ages= []

#print(sum(dfMale["Age"] < 10))
# First count # of people in each age bin
while EndAge <110:
	#print(str(StartAge) + ',' + str(EndAge))
	MaleAgeDat.append(sum((dfMale["Age"] >= StartAge) & (dfMale["Age"] < EndAge) & (dfMale["Survived"] == 1)))
	FemAgeDat.append(sum((dfFem["Age"] >= StartAge) & (dfFem["Age"] < EndAge) & (dfFem["Survived"] == 1)))
	X_ages.append(EndAge)
	StartAge = EndAge
	EndAge = EndAge + 10

#Now make bar plot
width = 2
plt.bar([elem-width/2 for elem in X_ages],MaleAgeDat,width, label = "Male")
plt.bar([elem+width/2 for elem in X_ages],FemAgeDat, width,label = "Female")
plt.xticks(range(0,110,10))
plt.title('Survival by Age and Gender')
plt.xlabel('Age')
plt.ylabel('Count')


plt.legend()
plt.show()

#print(MaleAgeDat)
#print(FemAgeDat)





