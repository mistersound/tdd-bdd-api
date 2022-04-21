import json
import argparse
parser = argparse.ArgumentParser(description='This tool serlize a BD json to RDF. Execution example:  Python3 BDserilizer.py -inputFile /Users/amirl/Downloads/BD.json -outputFile /Users/amirl/Downloads/BDinRDF.rdf ')
parser.add_argument('-inputFile', help='The path of the input File', required=True)
parser.add_argument('-outputFile', help='The path of the output File. If the file is not empty, its content will be overwritten.', required=True)
args = vars(parser.parse_args())
#read input file
f = open(args["inputFile"])
jsonLDFile = json.load(f)
#read output file
outputFile = open(args["outputFile"], "w")


#import the json
#with open(inputFile, 'r') as f:
    #jsonLDFile = json.load(f)

triples = []
triple = []
ID=buildingType=buildingNamethermalCapacityValue=thermalCapacityUnit=ConstructionYear=city=zipCode=adr=renovationYear=totalSpace=Floors=Tasks=Devices =""
try:
    ID = jsonLDFile["@id"]
    buildingType = jsonLDFile["@type"]
    buildingName = jsonLDFile["dco:hasName"]
    thermalCapacityValue = jsonLDFile["dco:hasThermalCapacity"][0]["@value"]
    thermalCapacityUnit = jsonLDFile["dco:hasThermalCapacity"][0]["dco:unit"]
    ConstructionYear = jsonLDFile["dco:hasConstructionYear"]
    city = jsonLDFile["dco:hasCity"]
    zipCode = jsonLDFile["dco:hasZipCode"]
    adr = jsonLDFile["dco:hasAddress"]
    renovationYear = jsonLDFile["dco:hasRenovationYear"]
    totalSpace = jsonLDFile["dco:hasTotalSpace"]
    Floors = jsonLDFile["Floors"]
    Tasks = jsonLDFile["Tasks"]
    Devices = jsonLDFile["Devices"]
except:
    pass
try:
    BuildingInstance=buildingName.replace(" ","")+ID
    outputFile.write('dco:'+BuildingInstance+ " " +"dco:hasID"+" "'"'+ID+'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance+ " " +"rdf:type"+" "+buildingType+" .\n")
    outputFile.write('dco:'+BuildingInstance+ " " +"dco:hasName"+" "'"'+buildingName+'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance+ " " +"dco:hasThermalCapacity"+" "+"dco:"+BuildingInstance+thermalCapacityValue+" .\n")
    outputFile.write('dco:'+BuildingInstance+thermalCapacityValue+ " " +"dco:hasThermalCapacityValue"+" "'"'+thermalCapacityValue+'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance+thermalCapacityValue+ " " +"dco:isMeasuredIn "+thermalCapacityUnit+" .\n")
    outputFile.write('dco:'+BuildingInstance+" "+"dco:hasConstructionYear"+" "'"'+ConstructionYear+'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance + " " + "dco:hasCity" +" "'"'+ city +'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance + " " + "dco:hasZipCode" +" "'"'+ zipCode +'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance + " " + "dco:hasRenovationYear" +" "'"'+ renovationYear+'"'+" .\n")
    outputFile.write('dco:'+BuildingInstance + " " + "dco:hasTotalSpace" +" "'"'+ totalSpace+'"'+" .\n")
except:
    pass

floorType=""
floorType2=""
spaces=""
idSpace=""
devices=[]
ExposedTasks=[]
#loop floors
#add the triples
deviceInstance=""
for Floor in Floors:
    #print("Floor=",Floor)
    outputFile.write('dco:'+BuildingInstance + " " + "dco:hasFloor " + "dco:"+ Floor +" .\n")

    try:
        floorType = Floors[Floor]["@type"]
        spaces = Floors[Floor]["dco:hasSpace"]
        ExposedTasks = Floors[Floor]["dco:isExposedToTask"]
        outputFile.write('dco:'+Floor + " " + "rdf:type" + " " + floorType +" .\n")
        for exposedTask in ExposedTasks:
            outputFile.write('dco:'+Floor + " " + "dco:isExposedToTsk "  + "dco:"+ exposedTask +" .\n")
        i = 0
        for space in spaces:
            idSpace = spaces[i]["@id"]
            typeSpace = spaces[i]["@type"]
            outputFile.write('dco:'+Floor+ " " +"dco:hasSpace "  + "dco:"+ idSpace +" .\n")
            outputFile.write('dco:'+ idSpace+ " " + "rdf:type" + " " + typeSpace+ " .\n")
            try:
                devices = spaces[i]["dco:hasDevice"]
                #print("all devices",devices)
                for device in devices:
                    outputFile.write('dco:'+ idSpace+" "+ "dco:hasDevice " + 'dco:'+ device +" .\n")
                    #print("device inst and space ",device)
            except:
                pass
            i += 1
    except:
        pass
#loop Tasks
AccomplishedTasks=[]
for Task in Tasks:
    taskType = Tasks[Task]["@type"]
    outputFile.write('dco:'+ Task + " " +"rdf:type" + " " + taskType + " .\n")
    #print("TaskType= ",taskType)
    AccomplishedBy = Tasks[Task]["dco:isAccomplishedBy"]
    for device in AccomplishedBy:
        #print("Device accomplished", device)
        outputFile.write('dco:'+ Task + " " +"dco:isAccomplishedBy " + 'dco:'+ device + " .\n")
#loop Devices
#deviceType
#
#print("Devices attribute")
for Device in Devices:
    deviceType = Devices[Device]["@type"]
    outputFile.write("dco:"+ device +" rdf:type" + " " + deviceType + " .\n")
    deviceJSON = Devices[Device]
    #interaction affordances
    for item in deviceJSON:
        #condition
        #print("all items",item)
        if ((str(item) != "hasObservableproperty") and (str(item) !=  "dco:observes") and (str(item) != "dco:hasHeatPumpRelay") and (str(item) != "dco:hasNominalPower") and (str(item) != "dco:hasVolume") and (str(item) != "dco:hasThingDescription") and (str(item) != "dco:hasMaximumOffTime")):
            print("")#dont do anything otherwise it will be a replication from the TDs
    #TD, dco:observes, @type, dco:hasObservableproperty, hasHeatPumpRelay,hasNominalPower, hasMaxOffTime, hasMinnOnTime
    try:
        observes = Devices[Device]["dco:observes"]
        #print("Observes=", observes )
        #for observation in observes:
            #print("itemObs",observes[observation]["@type"])
        #observedProperty =
    except:
        pass
    try:
        hasHeatPumpRelay = Devices[Device]["dco:hasHeatPumpRelay"]
        #print("hasHeatPumpRelay= ",hasHeatPumpRelay)
    except:
        pass
    try:
        hasObservablePropery = Devices[Device]["dco:hasObservablePropery"]
        for obsP in hasObservablePropery:
            #print("obsP",hasObservablePropery[obsP]["@type"])
            outputFile.write("dco:"+ device + " dco:hasObservablePropery" + " "'"' + obsP + " .\n")
            outputFile.write("dco:"+ obsP +" rdf:type" +" "+ hasObservablePropery[obsP]["@type"] +" .\n")

    except:
        pass
    try:
        hasNominalPower = Devices[Device]["dco:hasNominalPower"]
        #for nPower in hasNominalPower:
            #print("nPower",hasNominalPower[nPower])
    except:
        pass
    try:
        hasMaximumOffTime = Devices[Device]["dco:hasMaximumOffTime"]
        #for maxTimeItem in hasMaximumOffTime:
            #print("maxTimeItem",hasMaximumOffTime[maxTimeItem])
    except:
        pass
    try:
        hasMinimumOnTime = Devices[Device]["dco:hasMinimumOnTime"]
        #print("hasMinimumOnTime",hasMinimumOnTime)
        #for maxOnTimeItem in hasMinimumOnTime:
            #print("maxOnTimeItem",hasMinimumOnTime[maxOnTimeItem])
    except:
        pass
    #try:
        #hasVolume = Devices[Device]["dco:hasVolume"]
        #for hasVolumeItem in hasVolume:
            #print("hasVolumeItem",hasVolume[hasVolumeItem])
    #except:
        #pass
    try:
        hasThingDescription = Devices[Device]["dco:hasThingDescription"]
        outputFile.write("dco:"+ device +" dco:hasThingDescription" + " "'"' + hasThingDescription + '"' + " .\n")
    except:
        pass
outputFile.close()

print("done")
