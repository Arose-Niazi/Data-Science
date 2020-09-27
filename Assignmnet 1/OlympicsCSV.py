import pandas as pd


class Olympics:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.data.drop(index=["Totals"], inplace=True)
        self.fixNames()
        self.fixColumns()

        return

    def fixNames(self):
        countries = list(self.data.index)
        ids = list(self.data.index)
        x = 0
        while x < len(countries):
            ids[x] = str(ids[x])[str(ids[x]).find("(") + 1:str(ids[x]).find(")")]
            countries[x] = str(countries[x])[:str(countries[x]).find("(")]
            x += 1
        self.data.index = countries
        self.data['ID'] = ids
        return

    def fixColumns(self):
        lookingFor = ["01 !", "02 !", "03 !", "№"]
        replacingWith = ["Gold", "Silver", "Bronze", "#"]
        for column in self.data.columns:
            x = 0
            while x < len(lookingFor):
                if lookingFor[x] in column:
                    self.data.rename(columns={column: replacingWith[x]+column[len(lookingFor[x]):]}
                                     , inplace=True)
                x += 1
        return

    def getFirstCountry(self):
        return self.data.iloc[0]

    def mostSummerGolds(self):
        return self.data['Gold'].idxmax()

    def mostGoldDifference(self):
        difference = self.data['Gold']-self.data['Gold.1']
        mini = difference.idxmin()
        minimum = self.data.loc[mini]['Gold'] - self.data.loc[mini]['Gold.1']
        if minimum < 0:
            minimum *= -1

        maxi = difference.idxmax()
        most = self.data.loc[maxi]['Gold'] - self.data.loc[maxi]['Gold.1']
        if most > minimum:
            return maxi
        else:
            return mini

    def mostRelativeGoldDifference(self):
        goldMedalists = self.data.where((self.data['Gold'] > 0) & (self.data['Gold.1'] > 0))
        difference = (goldMedalists['Gold'] - goldMedalists['Gold.1'])/goldMedalists['Gold.2']
        mini = difference.idxmin()
        minimum = ((goldMedalists.loc[mini]['Gold'] - goldMedalists.loc[mini]['Gold.1'])
                   / goldMedalists.loc[mini]['Gold.2'])
        if minimum < 0:
            minimum *= -1

        maxi = difference.idxmax()
        most = ((goldMedalists.loc[maxi]['Gold'] - goldMedalists.loc[maxi]['Gold.1'])
                   / goldMedalists.loc[maxi]['Gold.2'])
        if most > minimum:
            return maxi
        else:
            return mini

    def calculatePoints(self):
        self.data['Points'] = (self.data['Gold.2'] * 3 + self.data['Silver.2'] * 2 + self.data['Bronze.2'] * 1)
        return self.data['Points']