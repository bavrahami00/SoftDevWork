# Benjamin Avrahami
# SoftDev pd9
# K10 -- Import/Export Bank
# 2020-03-04
# Team Opioids
"""
    Accidental Drug Related Deaths 2012-2018 Dataset
    This dataset contains a listing of each accidental drug-related death in the state of Connecticut. The dataset's contents include demgographic information about each victim, and a list of each drug found in their system.
    Data can be found at: https://data.ct.gov/api/views/rybz-nyjw/rows.json?accessType=DOWNLOAD
    The actual import mechanics were simple: data = json.load(file) - which is a one line mechanic, or two if you consider reading in the file as part of it.
    But it was more complicated because the actual data we needed was inside a 2d array within the dictionary, consisting of the list of people and their data. Therefore, for each person we created a dictionary, manually wrote in the keys (and there were roughly 30 of them), took their values, and inserted them into the mongo database.
"""

import json
#from bson.json_util import loads

from pymongo import MongoClient
client = MongoClient()
db = client["opioids"]
col = db["inventory"]

def setup():
    #col.remove({})
    if col.count_documents({}) == 0:
        with open('opioids.json','r') as file:
            data = json.load(file)
            #print(type(data))
            lis = data["data"]
            for item in lis:
                col.insert_one({"date": item[9], "datetype": item[10], "age": item[11], "sex": item[12], "race": item[13], "residencecity": item[14], "residencecounty": item[15], "residencestate": item[16], "deathcity": item[17], "deathcounty": item[18], "location": item[19], "locationifother": item[20], "descriptionofinjury": item[21], "injuryplace": item[22], "injurycity": item[23], "injurycounty": item[24], "injurystate": item[25], "cod": item[26], "othersignifican": item[27], "heroin": item[28], "cocaine": item[29], "fentanyl": item[30], "fentanylanalogue": item[31], "oxycodone": item[32], "oxymorphone": item[33],  "ethanol": item[34], "hydrocodone": item[35], "benzodiazepine": item[36], "methadone": item[37], "amphet": item[38], "tramad": item[39], "morphine_notheroin": item[40], "hydromorphone": item[41], "other": item[42], "opiatenos": item[43], "anyopioid": item[44], "mannerofdeath": item[45]})

def get_races():
    races = []
    for person in col.find():
        if person['race'] not in races:
            races.append(person['race'])
    #print(races)
    return races

#returns a dictionary of each race as the key and 0 as the value
# used in functions to count addicts by race
def get_race_dict():
    races = get_races()
    out = {}
    for race in races:
        out[race] = 0
    return out

#returns dictionary of all ages with 0 as value
#to be used by counter in later function
def get_age_dict():
    ages = []
    for person in col.find():
        if person['age'] not in ages:
            ages.append(person['age'])
    age_dict = {}
    for i in ages:
        age_dict[i] = 0
    return age_dict

def drug_list():
    #create list of all types of drugs
    dlist = ["heroin","cocaine","fentanyl","fentanylanalogue","oxycodone","oxymorphone","ethanol","hydrocodone","benzodiazepine","methadone","amphet","tramad","morphine_notheroin","hydromorphone","other"]
    ddict = {}
    for d in dlist:
        ddict[d] = col.find({d:"Y"}).count()
    print("The total number of people that had each drug in them:")
    #print data
    for d in dlist:
        print("\t",d,": ",ddict[d])

def all_drugs():
    dlist = ["heroin","cocaine","fentanyl","fentanylanalogue","oxycodone","oxymorphone","ethanol","hydrocodone","benzodiazepine","methadone","amphet","tramad","morphine_notheroin","hydromorphone","other"]
    return dlist

# prints demographic information about users of a collection of drugs
# drugs is an array of drug names
def getUsersInfo(drugs):
    # print all drugs in one line
    drug_string = ""
    for drug in drugs:
        drug_string = drug_string + drug
        drug_string = drug_string +", "
    drug_string = drug_string[:-2] #get rid of trailing ", "
    #create dictionary based on drugs in array
    drug_dict = {}
    for drug in drugs:
        drug_dict[drug] = "Y"
    #print(drug_dict)
    #find all people who match drugs dictionary
    addicts = col.find(drug_dict)
    #variables to store information about addicts:
    women,men= 0,0
    races = get_race_dict()
    ages = get_age_dict()
    for addict in addicts:
        if addict['sex'] == "Female":
            women = women + 1
        else:
            men = men + 1
        races[addict['race']] = races[addict['race']] + 1
        ages[addict['age']] = ages[addict['age']] + 1
    high_age = 0
    age = ""
    for a in ages:
        if ages[a] > high_age:
            high_age = ages[a]
            age = a
    #print info:
    print("\nInfo on users of ",drug_string)
    print(men,"men and",women,"women died.")
    print("The most affected age was",age,"with",high_age,"deaths.")
    print("Breakdown of deaths by race:")
    for race in races:
        print("\t",race,": ",races[race])
    if women == 0 and men == 0:
        print("\tNo data was found for the drugs you entered.")


def d_string(drugs):
    drug_string = ""
    for drug in drugs:
        drug_string = drug_string + drug
        drug_string = drug_string +", "
    drug_string = drug_string[:-2]
    return drug_string

def gender_deaths(drugs):
    drug_dict = {}
    for drug in drugs:
        drug_dict[drug] = "Y"
    addicts = col.find(drug_dict)
    women = 0
    men = 0
    other = 0
    for addict in addicts:
        if addict['sex'] == "Female":
            women = women + 1
        elif addict['sex'] == "Male":
            men = men + 1
        else:
            other = other + 1
    l = {}
    l["men"] = men
    l["women"] = women
    l["other"] = other
    return l

def age_deaths(drugs):
    drug_dict = {}
    for drug in drugs:
        drug_dict[drug] = "Y"
    addicts = col.find(drug_dict)
    ages = get_age_dict()
    for addict in addicts:
        ages[addict['age']] = ages[addict['age']] + 1
    return ages

def race_deaths(drugs):
    drug_dict = {}
    for drug in drugs:
        drug_dict[drug] = "Y"
    addicts = col.find(drug_dict)
    races = get_race_dict()
    for addict in addicts:
        races[addict['race']] = races[addict['race']] + 1
    return races
