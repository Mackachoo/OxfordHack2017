import json


def getJson(file):
    data = json.load(open(file,"r"))
    return data['Diseases']


def convertJsToPy(js):
    pureList = []
    for i in range(len(js)):
        tempList = [js[i]['Disease'],js[i]['Location'],js[i]['Race'],js[i]['Date'],js[i]['Medication']]
        pureList.append(tempList)
    return pureList

def cleaner(Value,Data,point):
    if Data == None:
        return []
    elif point == len(Data):
        return Data
    elif not (Value in Data[point] or Value in Data[point][4]) or (type(Value) != str and ((Value[0] == "T" and Value[1] <= Data[point][3]) or (Value[0] == "F" and Value[1] >= Data[point][3]))):
        del Data[point]
        return cleaner(Value,Data,0)
    else:
        return cleaner(Value,Data,point+1)
        print()

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
    medSet = convertJsToPy(getJson("medData.json"))
    for i in range(len(filters)):
        medSet = cleaner(filters[i],medSet,0)
    count = 1
    cleanList = []
    for cl in range(len(medSet)):
        cleanList.append(medSet[cl][1])
    medSet = CycleSort(cleanList)
    #print(medSet)
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

if __name__ == "__main__":
    print (RoadRunner(["White"]))