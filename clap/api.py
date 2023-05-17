import json
import requests
import sys
import time
from pprint import pprint

sysParse = len(sys.argv)
sysCounter = 1

while (sysCounter < sysParse):
		
		if (sys.argv[sysCounter] == "-help"):
			print ("")
			print ("Use: python3 api.py [flags]")
			print ("")
			print ("The following flags can be used to get information from the system:")
			print ("-jurisdictions -> list available jusrisdictions, along with API endpoints, slugs, and status")
			print ("Multiple flags can be used, e.g., python3 api.py -jusrisdictions -cases")
			print ("")


		if (sys.argv[sysCounter] == "-jurisdictions"):
			jxResponse = requests.get(
			'https://api.case.law/v1/jurisdictions/'
			)
            
			pprint (jxResponse.json())


		sysCounter = sysCounter + 1


#apiKey = 'YOUR_API_KEY'
requestURL = 'https://api.case.law/v1/jurisdictions/'



cases = 2

counter = 1
currentCase = 420005


#Specific jurisdiction

if (True):
	stateResponse = requests.get(
		'https://api.case.law/v1/cases/?q=cows&jurisdiction=ill&year=1984'
	)

	res = stateResponse.json()

	#pprint (res)


def jxSearch():
		
	jxWholeLoopBool = False

	while (jxWholeLoopBool == False):

		jxSearchLoopBool = False
		jxFileSelectorBool = False
		jxEndSelectorBool = False
		jxPageNumberBool = False

		print ("Please select a jurisdiction!")
		print ("You may use the jurisdiction flag on startup (-jurisdictions) to view all, or use an open jx from the list below.")
		print ("Illinois")
		print ("Arkansas")
		print ("New Mexico")
		print ("North Carolina")

		while (jxSearchLoopBool == False):
			print ("")
			jxAbbrevFull = input ("Please type a jurisdiction: ")

			if (jxAbbrevFull.lower() == "illinois" or jxAbbrevFull.lower() == "1" or jxAbbrevFull.lower() == "ill"):
				jxAbbrev = "ill"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "new mexico" or jxAbbrevFull.lower() == "nm" or jxAbbrevFull.lower() == "2"):
				jxAbbrev = "nm"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "north carolina" or jxAbbrevFull.lower() == "3" or jxAbbrevFull.lower() == "nc"):
				jxAbbrev = "nc"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "arkansas" or jxAbbrevFull.lower() == "4" or jxAbbrevFull.lower() == "ark"):
				jxAbbrev = "ark"
				jxSearchLoopBool = True
			else:
				print ("")
				print ("Sorry, invalid input!") 
				print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
				print ("")


		stateResponse = requests.get(
			('https://api.case.law/v1/cases/?jurisdiction=' + jxAbbrev)
		)
		res = stateResponse.json()

		totalJxCases = stateResponse.json()["count"]
		currentJxNext = stateResponse.json()["next"]

		totalPagesJx = int(((totalJxCases/100) + 1))


		while (jxFileSelectorBool == False):
			print ("")
			print ("Query completed")
			print ("")
			print ("Quick Stats:")
			print ("Total number of cases found: " + str(totalJxCases))
			print ("Total cases displayed per page: 100")
			print ("Total Pages: " + str(totalPagesJx))
			print ("")
			print ("How many pages of data would you like to see?")
			print ("You can enter a number from 1-" + str(totalPagesJx) + " or type \"all\" for all pages.")



			while (jxPageNumberBool == False):
				print ("")
				jxPagesSelection = input ("Please enter your selection here, as an integer (or all): ")
				print ("")

				if (jxPagesSelection.lower() == all):
					jxPagesSelection = str(totalPagesJx)

				if (jxPagesSelection.isdigit()):
					jxPagesSelection = int(jxPagesSelection)
					if ((jxPagesSelection > 0) and (jxPagesSelection <= totalPagesJx)):
						print ("Retrieving data...")
						jxPageNumberBool = True
					else:
						print ("")
						print ("Sorry, invalid input!") 
						print ("Please enter an integer between 1 and " + str(totalPagesJx) + "!")
						print ("")
				else:
					print ("")
					print ("Sorry, invalid input!") 
					print ("I'm a computer and I can be a little picky, please try entering an integer (e.g., 1, 2, 3, etc.!")
					print ("")


			#pagesLoop
			jxGetPageLoopCounter = 1

			while (jxGetPageLoopCounter < jxPagesSelection):
				stateResponseLoop = requests.get(
				(currentJxNext)
				)

				currentJxNext = stateResponseLoop.json()["next"]

				currentJxData = stateResponseLoop.json()["results"]

				for singleOne in currentJxData:
					res["results"].append(singleOne)
				
				jxGetPageLoopCounter = jxGetPageLoopCounter + 1
			

			print("")
			print ("You can display your results in your terminal or export a file to the current directory.")
			print ("Please note that displaying more than a page or two in a terminal can be overwhelming and messy.")
			jxPrintSelection = input("Please type \"terminal\" to display in terminal, \"file\" to export a file, or \"new\" to refine your search: ")
			print ("")

			if (jxPrintSelection.lower() == "terminal"):
					pprint (res)
					jxFileSelectorBool = True
			elif (jxPrintSelection.lower() == "file"):
				print ("Creating file...")
				with open('jurisdictionResults-' + jxAbbrev + '.txt', 'wt') as out:
					pprint(res, stream=out)
				jxFileSelectorBool = True
			elif (jxPrintSelection.lower() == "new"):
				print ("")
				print ("Returning to main menu...")
				print ("")
				jxEndSelectorBool = True
				jxFileSelectorBool = True
				jxWholeLoopBool = True
				time.sleep(2)
			else:
				print ("")
				print ("Sorry, invalid input!") 
				print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
				print ("")


		if (jxEndSelectorBool == False):
			print ("")
			print ("Would you like to run a new jurisdiction search, or return to the main menu? ")


		while (jxEndSelectorBool == False):

			print ("")
			jxEndSelection = input ("Please enter \"menu\" to return to the main menu, or \"new\" to run a new search: ")

			if (jxEndSelection.lower() == "menu"):
				print ("")
				print ("Returning to main menu...")
				print ("")
				time.sleep(1)
				jxEndSelectorBool = True
				jxWholeLoopBool = True
			elif (jxEndSelection.lower() == "new"):
				jxSearchLoopBool = False
				jxFileSelectorBool = False
				jxEndSelectorBool = True
				print ("")
				
			else:
				print ("")
				print ("Sorry, invalid input!") 
				print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
				print ("")

	jxEndSelectorBool = False
	


def wordSearch():
			
	wsWholeLoopBool = False

	while (wsWholeLoopBool == False):

		wordSearchList = []

		wsSearchLoopBool = False
		wsFileSelectorBool = False
		wsEndSelectorBool = False
		wsPageNumberBool = False
		wsAddWordBool = False
		jxSearchLoopBool = False
		wsAllBool = False
		allCasesDict = {}
		allCasePagesDict = {}

		print ("Search by keyword!")

		print ("To begin, please select a jurisdiction to search in.")
		print ("You may use the jurisdiction flag on startup (-jurisdictions) to view all, or use an open jx from the list below.")
		print ("Illinois")
		print ("Arkansas")
		print ("New Mexico")
		print ("North Carolina")
		print ("All Open Jurisdictions")

		while (jxSearchLoopBool == False):
			print ("")
			jxAbbrevFull = input ("Please type the full name of the jurisdiction, or type \"all\" to search all open jurisdictions: ")

			if (jxAbbrevFull.lower() == "illinois" or jxAbbrevFull.lower() == "1" or jxAbbrevFull.lower() == "ill"):
				jxAbbrev = "ill"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "new mexico" or jxAbbrevFull.lower() == "nm" or jxAbbrevFull.lower() == "2"):
				jxAbbrev = "nm"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "north carolina" or jxAbbrevFull.lower() == "3" or jxAbbrevFull.lower() == "nc"):
				jxAbbrev = "nc"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "arkansas" or jxAbbrevFull.lower() == "4" or jxAbbrevFull.lower() == "ark"):
				jxAbbrev = "ark"
				jxSearchLoopBool = True
			elif (jxAbbrevFull.lower() == "all" or jxAbbrevFull.lower() == "5"):
				jxAbbrev = "all"
				wsAllBool = True
				jxSearchLoopBool = True
			else:
				print ("")
				print ("Sorry, invalid input!") 
				print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
				print ("")


		while (wsSearchLoopBool == False):
			print ("")

			while (wsAddWordBool == False):
				wsAbbrevFull = input ("Please type a keyword and press enter: ")

				wsAbbrevPerm = wsAbbrevFull

				wordSearchList.append(wsAbbrevFull)

				innerWSloopBool = False

				while (innerWSloopBool == False):

					print ("")

					print ("Would you like to add any additional keywords?")
					wsAddMoreWords = input ("Please type \"yes\" or \"no\": ")


					if (wsAddMoreWords.lower() == "yes" or wsAddMoreWords.lower() == "y"):
						print ("")
						innerWSloopBool = True
					elif (wsAddMoreWords.lower() == "no" or wsAddMoreWords.lower() == "n"):
						print ("")
						print ("Compiling keywords...")
						print ("")
						wsAddWordBool = True
						innerWSloopBool = True
						wsSearchLoopBool = True
					else:
						print ("")
						print ("Sorry, invalid input!") 
						print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
						print ("")


		currentWordSearchString = ""
		wsTinyBool = False

		for eachWord in wordSearchList:
			if (wsTinyBool == False):
				currentWordSearchString = eachWord
				wsTinyBool = True
			else:
				currentWordSearchString = (currentWordSearchString + " " + eachWord)


		totalPagesws = 0

		if (jxAbbrev.lower() == "all"):
			jxArray = ['ill', 'ark', 'nm', 'nc']
			jxArrayFullNames = ["Illinois", "Arkansas", "New Mexico", "North Carolina"]

			caseTotalWord = 0
			caseLooperJx = 0

			for eachInJx in jxArray:
				keyResponse = requests.get(
				("https://api.case.law/v1/cases/?jurisdiction=" + eachInJx + "&search=" + currentWordSearchString)
				)
				res = keyResponse.json()

				caseTotalWord = caseTotalWord + keyResponse.json()["count"]

				allCasesDict[jxArrayFullNames[caseLooperJx]] = keyResponse.json()["count"]
				allCasePagesDict[jxArrayFullNames[caseLooperJx]] = int((((keyResponse.json()["count"]))/100) + 1)

				caseLooperJx = caseLooperJx + 1

			totalwsCasesFinal = caseTotalWord

			tempPageTracker = int(((caseTotalWord/100) + 1))
			
			totalPagesws = totalPagesws + tempPageTracker

		else:
			keyResponse = requests.get(
				("https://api.case.law/v1/cases/?jurisdiction=" + jxAbbrev + "&search=" + currentWordSearchString)
			)
			res = keyResponse.json()

			jxArray = [jxAbbrev]

			totalwsCases = keyResponse.json()["count"]
			totalwsCasesFinal = totalwsCases
			currentwsNext = keyResponse.json()["next"]

			totalPagesws = int(((totalwsCases/100) + 1))


		while (wsFileSelectorBool == False):
			print ("")
			print ("Query completed")
			print ("")
			print ("Quick Stats:")
			print ("Total number of cases found: " + str(totalwsCasesFinal))
			if (wsAllBool == True):
				tempIndvPageCounter = 0
				macroPageCounterWs = 0
				currentHighestPage = 1
				print ("Cases per jurisdiction: ")

				for jxKey, jxValue in allCasesDict.items():
					print ("")

					print (str(jxKey) + ": " + str(jxValue))
					macroPageCounterWs = macroPageCounterWs + int(((jxValue/100) + 1))
					tempIndvPageCounter = int(((jxValue/100) + 1))
					print ("Pages: " + str(tempIndvPageCounter))

					if (tempIndvPageCounter > currentHighestPage):
						currentHighestPage = tempIndvPageCounter
				
				print ("")
				print ("Total cases displayed per page: 100")
				print ("Total Pages: " + str(macroPageCounterWs))

				print ("")
				print ("How many pages of data would you like to see per jurisdiction?")
				print ("You can enter a number between 1 and " + str(currentHighestPage) + " or type \"all\" for all pages.")

			else:
				print ("")
				print ("Total cases displayed per page: 100")
				print ("Total Pages: " + str(totalPagesws))
				print ("")
				print ("How many pages of data would you like to see?")
				print ("You can enter a number between 1 and " + str(totalPagesws) + " or type \"all\" for all pages.")



			while (wsPageNumberBool == False):
				print ("")
				wsPagesSelection = input ("Please enter your selection here, as an integer (or all): ")
				print ("")

				if (wsPagesSelection.lower() == all):
					jwsPagesSelection = str(totalPagesws)

				if (wsPagesSelection.isdigit()):
					wsPagesSelection = int(wsPagesSelection)
					if ((wsPagesSelection > 0) and (wsPagesSelection <= totalPagesws)):
						print ("Retrieving data...")
						wsPageNumberBool = True
					else:
						print ("")
						print ("Sorry, invalid input!") 
						print ("Please enter an integer between 1 and " + str(totalPagesws) + "!")
						print ("")
				else:
					print ("")
					print ("Sorry, invalid input!") 
					print ("I'm a computer and I can be a little picky, please try entering an integer (e.g., 1, 2, 3, etc.!")
					print ("")


			if (wsAllBool == True):

				firstWsGrabLoopBool = True
				eachNewLoopBool = True

				for grabKey, grabValue in allCasePagesDict.items():

					caseLooperJx = 0

					if (grabKey == "Illinois"):
						grabKey = "ill"
					elif (grabKey == "Arkansas"):
						grabKey = "ark"
					elif (grabKey == "New Mexico"):
						grabKey = "nm"
					elif (grabKey == "North Carolina"):
						grabKey = "nc"

					while (caseLooperJx < grabValue):

						if (firstWsGrabLoopBool == True):
							keyResponseLoop = requests.get(
							("https://api.case.law/v1/cases/?jurisdiction=" + grabKey + "&search=" + currentWordSearchString)
							)
							res = keyResponseLoop.json()

							firstWsGrabLoopBool = False

							currentwsNext = keyResponseLoop.json()["next"]

							caseLooperJx = caseLooperJx + 1

						elif (eachNewLoopBool == True):
							keyResponseLoop = requests.get(
							("https://api.case.law/v1/cases/?jurisdiction=" + grabKey + "&search=" + currentWordSearchString)
							)
							resTemp = keyResponseLoop.json()

							currentWsDataLoop = keyResponseLoop.json()["results"]

							for singleOne in currentWsDataLoop:
								res["results"].append(singleOne)

							currentwsNext = keyResponseLoop.json()["next"]
							eachNewLoopBool = False

							caseLooperJx = caseLooperJx + 1
						
						else: 
							keyResponseLoop = requests.get(
							(currentwsNext)
							)
							resTemp = keyResponseLoop.json()

							currentwsNext = keyResponseLoop.json()["next"]

							currentWsDataLoop = keyResponseLoop.json()["results"]

							for singleOne in currentWsDataLoop:
								res["results"].append(singleOne)

							caseLooperJx = caseLooperJx + 1

						if (caseLooperJx == grabValue):
							eachNewLoopBool = True
			
			else:

				wsGetPageLoopCounter = 1

				while (wsGetPageLoopCounter < wsPagesSelection):
					keyResponseLoop = requests.get(
					(currentwsNext)
					)

					currentwsNext = keyResponseLoop.json()["next"]

					currentwsData = keyResponseLoop.json()["results"]

					for singleOne in currentwsData:
						res["results"].append(singleOne)
					
					wsGetPageLoopCounter = wsGetPageLoopCounter + 1
			

			print("")
			print ("You can display your results in your terminal or export a file to the current directory.")
			print ("Please note that displaying more than a page or two in a terminal can be overwhelming and messy.")
			wsPrintSelection = input("Please type \"terminal\" to display in terminal, \"file\" to export a file, or \"new\" to refine your search: ")
			print ("")

			if (wsPrintSelection.lower() == "terminal"):
					pprint (res)
					wsFileSelectorBool = True
			elif (wsPrintSelection.lower() == "file"):
				print ("Creating file...")
				with open('keywordResults-' + wsAbbrevPerm + '.txt', 'wt') as out:
					pprint(res, stream=out)
				wsFileSelectorBool = True
			elif (wsPrintSelection.lower() == "new"):
				print ("")
				print ("Returning to main menu...")
				print ("")
				wsEndSelectorBool = True
				wsFileSelectorBool = True
				wsWholeLoopBool = True
				time.sleep(2)
			else:
				print ("")
				print ("Sorry, invalid input!") 
				print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
				print ("")


		if (wsEndSelectorBool == False):
			print ("")
			print ("Would you like to run a new keyword search, or return to the main menu? ")


		while (wsEndSelectorBool == False):

			print ("")
			wsEndSelection = input ("Please enter \"menu\" to return to the main menu, or \"new\" to run a new search: ")

			if (wsEndSelection.lower() == "menu"):
				print ("")
				print ("Returning to main menu...")
				print ("")
				time.sleep(1)
				wsEndSelectorBool = True
				wsWholeLoopBool = True
			elif (wsEndSelection.lower() == "new"):
				wsSearchLoopBool = False
				wsFileSelectorBool = False
				wsEndSelectorBool = True
				print ("")
				
			else:
				print ("")
				print ("Sorry, invalid input!") 
				print ("I'm a computer and I can be a little picky, please check your spelling and try again!")
				print ("")

	wsEndSelectorBool = False

def yearSearch():
	print("3")

def caseSearch():
	print("")
	print ("This is still under construction! Working on it, please be patient (or check the docs :)")
	print ("")

def viewInstructions():
	print ("")
	print ("Use: python3 api.py [flags]")
	print ("")
	print ("The following flags can be used to get information from the system:")
	print ("-jurisdictions -> list available jusrisdictions, along with API endpoints, slugs, and status")
	print ("Multiple flags can be used, e.g., python3 api.py -jusrisdictions -cases")
	print ("")
	print ("Otherwise, to search, you can elect to search cases by jurisdiction, case number (if known), citations, year, keyword, or a combination.")
	print ("Please note that the only open-access US jurisdictions are IL, AR, NM, and NC.") 
	print ("All other jurisdictions require registration (https://case.law/user/register/) and have a 500-query limit per day.")
	print ("You can elect to get this data in JSON format or raw text format, as well as leave it in your terminal or receive a file.")
	print ("You may look up more advanced features by visiting the documentation: https://case.law/docs/site_features/api")
	print ("")

	helpLoopBool = False

	while (helpLoopBool == False):
		helpSelection = input ("Please enter \"menu\" to be returned to the main menu, or \"exit\" to quit the program:  ")
		print ("")

		helpSelection = helpSelection.lower()

		if (helpSelection == "menu"):
			print ("You will now be returned to the main menu. Thanks!")
			time.sleep(2)
			helpLoopBool = True
			return False
		elif (helpSelection == "exit"):
			print ("")
			print ("Thanks! Exiting...")
			print ("")
			time.sleep(1)
			helpLoopBool = True
			return True
		else:
			print ("Sorry, invalid input!") 
			print ("I'm a computer and I can be a little picky, please try again with checked spelling, without spaces, etc...")
			print ("")
			time.sleep(2)

	print ("")


while (counter < cases):
	#currentCase = currentCase + 1
	response = requests.get(
		'https://api.case.law/v1/ngrams/?q=raisins&jurisdiction=ill&year=1984',
		#headers={'Authorization': 'Token ' + apiKey }
	)

	counter = counter + 1

	res = response.json()

	#pprint (res)

	text = response.json()



def main():
	
	loopBool = False

	while (loopBool == False):
		print ("")
		print ("Welcome to the Case Law Access Project API, from Harvard Law School's Library Innovation Lab!")
		print ("You can visit the website at: https://case.law/")
		
		#How to search
		print ("")
		print ("How would you like to search?")
		print ("1. By Jurisdiction")
		print ("2. By Keyword")
		print ("3. By Year")
		print ("4. By Case Number")
		print ("5. View Instructions")

		print ("")

		caseSelector = input("Enter your selection (1-4) and press enter, or enter \"5\" to view the instructions:  ")
		print("")



		if (caseSelector == "1"):
			jxSearch()
		elif (caseSelector == "2"):
			wordSearch()
			#https://api.case.law/v1/cases/?search=keyword
		elif (caseSelector == "3"):
			yearSearch()
		elif (caseSelector == "4"):
			caseSearch()
		elif (caseSelector == "5"):
			testBool = viewInstructions()
			if (testBool == True):
				loopBool = True
		else:
			print ("Invalid input!")
			print ("I'm a computer and I can be a little picky, please try again with checked spelling, without spaces, etc...")
			print ("Regenerating menu...")
			print ("")
			time.sleep (3)


if __name__ == "__main__":
    main()
