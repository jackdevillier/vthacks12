#Libraries to Import
import csv
import json

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
    for i in range(len(States)):
        data, total = ReadCsv(States[i])
        data = ConvertData(data)
        JSONDump(States[i], data)
        JSONDumpTot(States[i], total)
    Cities, Acro = (ConvertDataCities(LGBTQCities()))
    JSONDumpCities(Acro, Cities)

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

def ConvertData(data):
    dict = {}
    for o in range(0, len(data),2):
        dict[o] = data[o]
        dict[o+1] = data[o+1]
    return dict

#JSON File Dump
def JSONDump(State, Data):
    json_object = json.dumps(Data, indent=4)
    File_Name = "JSONFolder\\"+ State
    with open(File_Name, "w") as outfile:
        outfile.write(json_object)

def JSONDumpTot(State, Total):
    json_object = json.dumps(Total, indent=4)
    File_Name = "JSONTot\\"+ State + "Tot"
    with open(File_Name, "w") as outfile:
        outfile.write(json_object)


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

def ConvertDataCities(data):
    dict = {}
    Acronym = [0]*len(data)
    for o in range(0, len(data),2):
        dict[o] = data[o][0]
        dict[o+1] = data[o][2]
        Acronym[o] = str(data[o][1])
    return dict, Acronym

def JSONDumpCities(Acro, Cities):
    json_object = json.dumps(Cities, indent=4)
    for p in range(0, len(Acro),2):
        json_object = json.dumps(Cities[p]+Cities[p+1], indent=4)
        print(Acro)
        Acro[p] = Acro[p].replace('"', "")
        File_Name = "JSONCityRanks\\"+ Acro[p]
        with open(File_Name, "w") as outfile:
            outfile.write(json_object)

# Runs main
main()
