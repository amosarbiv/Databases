import urllib.request
import json
from collections import defaultdict
from random import randint

def ReadData(fname, listData):
    with open(fname) as f:
        listData = f.readlines()
        listData = [x.strip() for x in listData]
    return listData

def main():
    MaleFirstNames = []
    FemaleFirstNames = []
    LastNames = []
    Countries = []
    Ages = []
    output_list = list()
    MaleFirstNames = ReadData("Users//MaleFirst.txt",MaleFirstNames)
    FemaleFirstNames = ReadData("Users//FemaleFirst.txt",FemaleFirstNames)
    LastNames = ReadData("Users//LastNames.txt",LastNames)
    Countries = ReadData("Users//Countries.txt",Countries)
    Ages = ReadData("Users//Ages.txt",Ages)
    countFirst = 0
    countLast = 0
    idc = 0
    output_dict = defaultdict()
    while (countFirst < len(MaleFirstNames)):
        if ( len(output_dict) > 0 ):
            output_list.append(output_dict)
            output_dict = defaultdict()
                
        age = randint(0, len(Ages)-1)
        country = randint(0, len(Countries)-1)
        output_dict["UserId"] = idc
        output_dict["FirstName"] = MaleFirstNames[countFirst]
        output_dict["LastName"] = LastNames[countLast]
        output_dict["Gender"] = "Male"
        output_dict["Age"] = Ages[age]
        output_dict["Country"] = Countries[country]
                        
        idc += 1
        countFirst += 1
        countLast += 1
        if(countLast == len(LastNames)):
            countLast = 0
                
    countFirst = 0          
    while (countFirst < len(FemaleFirstNames)):
        if ( len(output_dict) > 0 ):
            output_list.append(output_dict)
            output_dict = defaultdict()
                
        age = randint(0, len(Ages)-1)
        country = randint(0, len(Countries)-1)
        output_dict["UserId"] = idc
        output_dict["FirstName"] = FemaleFirstNames[countFirst]
        output_dict["LastName"] = LastNames[countLast]
        output_dict["Gender"] = "Female"
        output_dict["Age"] = Ages[age]
        output_dict["Country"] = Countries[country]
                        
        idc += 1
        countFirst += 1
        countLast += 1
        if(countLast == len(LastNames)):
            countLast = 0
            
    
    f = open("Tables//UsersTable.json","w")
    json.dump(output_list, f)
        


if __name__ == "__main__":
        main()

