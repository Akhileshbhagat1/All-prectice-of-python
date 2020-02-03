import pandas as pd


# ABC_web = {'day': [1, 2, 3, 4, 5, 6], "Visitors": [1000, 750, 6000, 450, 1000, 950], "Bounce_rate": [20, 25, 30, 15, 20, 24]}
# df = pd.DataFrame(ABC_web)
# print(df.head(2))

#We can marge Two or more dataframes into one dataframes
#
# df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 56, 67]},
#                    index=[2001, 2002, 2003, 2004])
# df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 56, 67]},
#                    index=[2005, 2006, 2007, 2008])
#merge = pd.merge(df1, df2)
# merge = pd.merge(df1, df2, on="HPI")
# print(merge)

# We can perform joined operaion
#
# df1 = pd.DataFrame({"Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
#                    index=[2001, 2002, 2003, 2004])
# df2 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment":[1, 3, 5, 6]},
#                    index=[2001, 2003, 2004, 2004])
# joined = df1.join(df2)
# print(joined)


# Changing the Index & Column Headers

# df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors":[200, 100, 300, 400], "Bounce_Rate": [20, 45, 60, 10]})
# # df.set_index("Day", inplace=True)
#
# df = df.rename(columns={"Visitors": "Users"})
# print(df)

#we can perform Concatination of data
#
# df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 56, 67]},
#                    index=[2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 56, 67]},
#                     index=[2005, 2006, 2007, 2008])
#
# concat = pd.concat([df1, df2])
# print(concat)


