#Libraries to Import
import csv


# Global
States = ["Alabama", "Alaska", "Arizona","Arkansas","California","Colorado",
          "Connecticut", "Delaware","District of Columbia", "Florida", "Georgia",
          "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
          "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
          "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
          "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]

StatesShorten = ["AL", "AK", "AZ", "AR", "CA", "CO","CT","DE", "DC","FL","GA",
                 "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI",
                 "MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH",
                 "OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV",
                 "WI","WY"]



# Main
def main():
    print("")
    for i in range(len(States)):
        print(States[i], ReadCsv(States[i]))
        print("")
        print("---------------------------------------------")
        print("")
    print(LGBTQCities())

#
# Functions
#

#United States of Hatecrimes
# Data Collection
def ReadCsv(state):
    data = []
    type = []
    amount = []
    File_Name = state + " Bias Types 2022.csv"
    File_Name = "Data Folder\\United States of Hatecrimes\\" + File_Name
    with open(File_Name, mode='r') as csvfile:
        file = csv.reader(csvfile)
        for row in csvfile:
            data.append(row)
    data[0] = "Type,Amount"
    for i in range(len(data)):
        data[i] = data[i].replace('\n','')
        data[i] = data[i].split(",")
    total, data = CheckLGBTQ(data)
    return data, total

#Checking data from list for LGBTQ+ Hate Crimes
def CheckLGBTQ(data):
    total = 0
    Marked = []
    KeyWords = ["Gay", "Lesbian", "Bisexual", "Transgender", "Non-conforming"]
    for i in range(len(data)):
        for j in range(len(KeyWords)):
            if data[i][0].find(KeyWords[j]) != -1:
                total = total + int(data[i][1])
                Marked.append([data[i][0],data[i][1]])
            else:
                pass
    return total, Marked    

#MostLGBTQ+ Cities
#Gathers cities data
def LGBTQCities():
    data = []
    File_Name = "Data Folder\\Most LGBT Friendly Cities 2023.csv"
    with open(File_Name, mode='r') as csvfile:
        for row in csvfile:
            data.append(row)
        for i in range(len(data)):
            data[i] = data[i].split(",")
            data[i].pop(8)
            data[i].pop(7)
            data[i].pop(6)
            data[i].pop(5)
            data[i].pop(4)
            data[i].pop(0)
        data.pop(0)
    return GayestCityFinder(data)

#Queerest City Per State
def GayestCityFinder(data):
    GayestCity = []
    StatesShortenTemp = StatesShorten
    for j in range(len(StatesShorten)):
        w = 0
        pop = False
        while w < 200 and pop == False:
            if data[w][1].find(StatesShortenTemp[0]) != -1:
                GayestCity.append([data[w][0],data[w][1],data[w][2]])
                pop = True
                StatesShortenTemp.pop(0)
                break
            elif data[w][1].find(StatesShortenTemp[0]) == -1 and w == 199:
                StatesShortenTemp.pop(0)
            w = w + 1
    return GayestCity

        

# Runs main
main()
