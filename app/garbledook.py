import json

def getJson(file):
    data = json.load(open(file,"r"))
    return data

def whoahWhatIsThis(js):
    pureList = []
    for i in js:
        subList = js[str(i)]

        try:
            DateList = [(subList["Date"])] + subList["DateList"]
        except:
            DateList = subList["DateList"]

        try:
            DisList = [(subList["Disease"])] + subList["DiseaseList"]
        except:
            DisList = subList["DiseaseList"]

        if len(DateList) != 0 and len(DisList) != 0:
            currLoc = subList["Location"]
            currRace = subList["Race"]
            currMed = subList["Medication"]

            Count = 0
            while Count < len(DateList) and Count < len(DisList):
                cleanList = [DisList[Count]] + [currLoc] + [currRace] + [DateList[Count]] + [currMed]
                pureList.append(cleanList)
                Count += 1
    return pureList

def convertJsToPy(js):
    pureList = []
    for i in range(len(js)):
        tempList = [js[i]['Disease'],js[i]['Location'],js[i]['Race'],js[i]['Date'],js[i]['Medication']]
        pureList.append(tempList)
    return pureList

def cleaner(Value,Data):
    point = 0
    while point < len(Data):
        if not (Value in Data[point] or Value in Data[point][4]) or (type(Value) != str and ((Value[0] == "T" and Value[1] >= Data[point][3]) or (Value[0] == "F" and Value[1] <= Data[point][3]))):
            del Data[point]
        else:
            point += 1
    return Data

def loader(Data):
    locs = []
    for i in range(len(Data)):
        locs.append(Data[i][1])
    return locs

def CycleSort(List):
    for cycLoc in range(len(List)):
        pos = cycLoc + 1
        while pos != cycLoc:
            pos = cycLoc
            for index in List[cycLoc+1:]:
                if index < List[cycLoc]:
                    pos += 1
            if pos != cycLoc:
                while List[cycLoc] == List[pos]:
                    pos += 1
                List[pos], List[cycLoc] = List[cycLoc], List[pos]
    return List


def RoadRunner(filters):
    medSet = whoahWhatIsThis(getJson("output.json"))
    for i in range(len(filters)):
        medSet = cleaner(filters[i],medSet)
    count = 1
    cleanList = []
    for cl in range(len(medSet)):
        cleanList.append(medSet[cl][1])
    medSet = CycleSort(cleanList)
    dim2Set = []
    for ind in range(len(medSet)):
        if ind + 1 == len(medSet):
            dim2Set.append([medSet[ind], count])
        elif medSet[ind] == medSet[ind+1]:
            count += 1
        else:
            dim2Set.append([medSet[ind],count])
            count = 1
    return dim2Set