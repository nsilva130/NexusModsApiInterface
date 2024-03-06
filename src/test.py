#!/usr/bin/env python

import sys
from Engine import NexusApi
from Engine import InputManager

import time
from datetime import datetime, timezone
import json
import io
from pathlib import Path
import webbrowser

# The function to be executed at runtime
def main():
    # Initialize API interface
    # Request API Key from user
    apiKey = input("Enter API Access Key: ")
    nexusMods = NexusApi(apiKey)
    
    # Game to search for mods
    gameDomain = "baldursgate3"
    
    
    # Test if file exists
    fileName = input("Enter mod list json file name: ")
    fileDirectory = "src/ModLists/"
    fileExtension = ".json"
    filePath = Path(fileDirectory + fileName)
    if (fileName[-len(fileExtension):] != fileExtension):
        print("File name "+ fileName + " missing extension. Appending '.json' to end.")
        filePath = Path(fileDirectory + fileName + fileExtension)
    
    
    
    inputModList = None
    modIdList = []
    
    
    if Path.exists(filePath):
        f = open(filePath)
        inputModList = json.load(f)
        print("Loaded File '" + fileName + "' successfully!")
        print("File Contents: " + json.dumps(inputModList))
        f.close()
        for mod in inputModList:
            modIdList.append(mod["id"])
    else:
        print("Filename '" + fileName + "' not found!")
        # If original mod list cannot be found, prompt user for input
        continueOnFileNotFound = InputManager.falsyBooleanInput("Continue script (y/*)? ", "y")
        # If the user wants to continue
        if (continueOnFileNotFound):
            print("Continuing script!")
        else:
            print("Stopping script!")
            return
    
    # Get count of original mods
    inputCount = len(modIdList)
    
    ########
    # Fill later
    ########
    
    # Placeholder: Hardcoded modlist file
    addModIdList = [125,642,899,1779,2435,1333,141,744,97,1416,1028,2417,206,432,2714,1933,2342,3619,1713,1323,2700,2515,2663,1148,3938,167,366,1363,1247,831,3000,422,2786,394,629,716,1529,1280,327,2996,1771,2896,2460,2672,189,2027,1902,1085,2424,213,457,1345,377,1729,4496,5808,3888,1820,5822]
    
    # check additional mod IDs and add if missing
    for modId in addModIdList:
        if not modId in modIdList:
            modIdList.append(modId)
            print("Added modId " + str(modId) + " to list.")
        else:
            print("ModId " + str(modId) + " already in loaded file, ignoring!")
    
    
    #modList = [{"id": 125, "lastUpdated": yyyymmddhhmmss, "url": },{"id": 642, "lastUpdated": None},{"id": 899, "lastUpdated": None},{"id": 1779, "lastUpdated": None}]
    
    print("List of modIds to check: " + str(modIdList))
    
    outputModList = []
    updatesRequired = []
    
    totalMods = len(modIdList)
    
    # Check all modIds on NexusMods while tracking index
    for index,modId in enumerate(modIdList):
        print("Checking modId="+str(modId) + " (mod #" + str(index+1) + "/" + str(totalMods) + ")")
        outputMod = {"name": None,"id": None,"updatedTimestamp": None,"updatedTime":None,"lastDownloaded":None,"url":None}
        getMod = nexusMods.getMod(game=gameDomain,id=modId)
        getModJson = getMod.json()
        
        # Assemble Mod Info
        outputMod["name"] = getModJson["name"]
        outputMod["id"] = modId
        outputMod["updatedTimestamp"] = getModJson["updated_timestamp"]
        outputMod["updatedTime"] = getModJson["updated_time"]
        outputMod["url"] = "https://www.nexusmods.com/"+gameDomain+"/mods/"+str(modId)
        
        
        # Compare updatedTimestamp and lastUpdated timestamps
        
        # If it is before the end of the original list, run standard check. Else, automatically add to flagged update list
        if (index < inputCount):
            # If it doesn't have a timestamp, default to adding it to the list
            if (not inputModList[index]["lastDownloaded"]):
                print("modId="+ str(modId) +" doesn't have lastDownloaded, flagging for update!")
                updatesRequired.append(index)
            else:
                # Copy old download timestamp
                outputMod["lastDownloaded"] = inputModList[index]["lastDownloaded"]
                
                # Process timestamps
                lastDownloadedTime = datetime.fromisoformat(outputMod["lastDownloaded"])
                lastUpdatedTime = datetime.fromisoformat(outputMod["updatedTime"])
                
                # Change lastUpdatedTime to match lastDownloaded timezone
                lastDownloadedTimezone = lastDownloadedTime.tzinfo
                lastUpdatedTime = lastUpdatedTime.astimezone(lastDownloadedTimezone)
                
                # Compare the times to determine if an update occured since lastDownloaded
                if (lastDownloadedTime < lastUpdatedTime):
                    print("modId="+ str(modId) +" has updated since lastDownloaded, flagging for update!")
                    updatesRequired.append(index)
        else:
            # Mod is new, needs to initialize update
            print("modId="+ str(modId) +" is new mod, flagging for update!")
            updatesRequired.append(index)
        
        outputModList.append(outputMod)
        time.sleep(0.1)
    
    
    if (len(updatesRequired) > 0):
        print(str(len(updatesRequired)) + " mod(s) flagged for updates!")
        # If the mods should be checked for updates. 
        # Boolean. Will default to "False" on invalid input
        addressUpdates = InputManager.falsyBooleanInput("Address updates (y/*)? ", "y")
        
        # If positive input received
        if (addressUpdates):
            
            batchUpdate = InputManager.falsyBooleanInput("Open links en masse (y/*, will open all at once)? ", "y")
            batchLinks = []
            
            timeNow = datetime.now().astimezone(timezone.utc).isoformat(timespec='microseconds')
            # For each index flagged, address updates individually
            for index in updatesRequired:
                # Assemble mod info for use
                modName = outputModList[index]["name"]
                modId = outputModList[index]["id"]
                modUrl = outputModList[index]["url"]
                modUpdatedTime = outputModList[index]["updatedTime"]
                modLastDownloaded = outputModList[index]["lastDownloaded"]
                modIsNew = (not (index < inputCount))
                
                # Print mod info
                print("\nMod Name: " + str(modName))
                print("Mod ID: " + str(modId))
                print("URL: " + str(modUrl))
                print("Mod is new: " + str(modIsNew))
                print("Repo Updated: " + str(modUpdatedTime))
                print("Last Downloaded: " + str(modLastDownloaded))
                
                # Ask if you want to address this specific update
                addressModUpdate = InputManager.falsyBooleanInput("Open modpage (y/*)? ", "y")
                if (addressModUpdate):
                    # If batch links are enabled, add to list of links to open
                    if (batchUpdate):
                        batchLinks.append(modUrl)
                    else:
                        # Open the mod individually and prompt for input when done
                        webbrowser.open(modUrl)
                        # Wait for user input before proceeding
                        input("Press enter/return when ready to continue...")
                
                # Ask if you want to update lastDownloaded to current time
                addLastDownloaded = InputManager.falsyBooleanInput("Add current time as lastDownloaded (y/*)? ", "y")
                if (addLastDownloaded):
                    outputModList[index]["lastDownloaded"] = timeNow
                    
                
            if (batchUpdate and (len(batchLinks) > 0) ):
                print("Opening " + str(len(batchLinks)) + " mod page(s)! This may take a minute...")
                for link in batchLinks:
                    webbrowser.open(link)
                    time.sleep(0.5)
                
                print("Finished opening " + str(len(batchLinks)) + " mod pages!")
            
            
            print("Finished addressing updates!")
        else:
            # Negative input was received
            print("Ignoring updates!")
    
    
    
    
    
    
    # Print final outputModList result
    print(outputModList)
    
    # Save to file
    
    # Generate new file name
    outputFileName = fileName
    
    newFileName = InputManager.falsyBooleanInput("New file name (y/*)? ", "y")
    
    if (newFileName):
        outputFileName = input("Enter new file name: ")
    
    
    # Remove file extension if it exists
    if (outputFileName[-len(fileExtension):] == fileExtension):
        outputFileName = outputFileName[:-len(fileExtension)]
        
    # Generate default output file path
    outputFileDirectory = fileDirectory + "Results/"
    outputFilePath = Path(outputFileDirectory + outputFileName + fileExtension)
    
    
    # If the output file name already exists, increase increment until new file name is reached
    if Path.exists(outputFilePath):
        print(outputFileName + fileExtension + " already exists!")
        index = 0
        while Path.exists(outputFilePath):
            index += 1
            outputFilePath = Path(outputFileDirectory + outputFileName + " (" + str(index) + ")" + fileExtension)
    
    
    print("Saving data as '"+ str(outputFilePath) +"'")
    
    # Save output contents
    with open(outputFilePath, 'w', encoding='utf-8') as f:
        json.dump(outputModList, f, ensure_ascii=False, indent=4)
    
if __name__ == '__main__':
    main()