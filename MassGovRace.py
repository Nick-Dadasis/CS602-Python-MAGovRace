'''
=======================================================
Created on 03/17/23
CS602 Spring 2023 Assignment 3
=======================================================
Student will use conditional statements
for/while loops, and multi-dimensional lists
to determine the Massachusetts county x totals
from the city x totals.
@author: Nick Dadasis
=======================================================
'''
import copy # using the deep copy function from the copy module
import csv  # import the csv module to read in the csv data

'''
======================================
This code set these variables that
are used to indicate which column
in the csv files contain needed data.
======================================
'''
cityCol = 0
candidateCol = 1
countyCol = 1
partyCol = 2
voteCol = 3

'''
================================================
processDataFiles Function
================================================
This function processes the csv files that
contains all the data into 3 multi-dimensional
lists. The function returns the 3 lists
back to the main function.
================================================
'''
def processDataFiles():
    with open('MassGovVotes.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        totalVotesCandidateCity = list(reader)
    f.close()

    with open('City_To_County.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        cityCounty = list(reader)
    f.close()

    with open('MassGovVoteTotalsCounty.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        totalCountyVotes = list(reader)
    f.close()

    return totalVotesCandidateCity, cityCounty, totalCountyVotes

'''
=======================================================
convertCityToCounty Function
=======================================================
This function takes the data in the list 
cityCandidateVoteList which contains x
counts by city and changes the city entry in the list
to the county that the city is in.
=======================================================
'''
def convertCityToCounty(votesByCandidateCityLst, cityCountyList):
    '''
    This function uses nested for loops to loop through the cityCountyList and votesByCandidateCityLst while using an if statement to check if the city in the
    votesByCandidateCityLst matches the city in cityCountyList. If it does, a new list (candidateCountyVotes) is created that stores the county from the cityCountyList
    and the candidate, party, votes, and if they won from the votesByCandidateCityLst. This new list is then appended to the votesByCandidateCountyLst, which 
    happens each time the code loops. Once the loop is finished, the new multidimensional list votesByCandidateCountyLst is returned to the main() function.
    '''
    
    votesByCandidateCountyLst = []
    
    for city in cityCountyList:
        for x in votesByCandidateCityLst:
            if x[0] == city[0]:
                candidateCountyVotes = []
                candidateCountyVotes.append(city[1])
                candidateCountyVotes.append(x[1])
                candidateCountyVotes.append(x[2])
                candidateCountyVotes.append(x[3])
                candidateCountyVotes.append(x[4])
                votesByCandidateCountyLst.append(candidateCountyVotes)
    return votesByCandidateCountyLst        
    
'''
================================================================
getCandidates Function
================================================================
This function takes the data in the list cityByCandidateVoteLst 
and retrieves and returns the names of the 3 
candidates (Democrat, Republican, Libertarian).
================================================================
'''
def getCandidates(cityByCandidateCountyLst):
    '''
    This function uses a for loop to loop through cityByCandidateCountyLst and if-elif statements to find "DEM", "REP", or "LIB" within the multidimensional
    list. Once these values are identified, the specific position of each candidate are set equal to candDem, candRep, and candLib, which are then returned to
    the main() function.
    '''
    
    for cand in cityByCandidateCountyLst:
        if cand[2] == "DEM":
            candDem = cityByCandidateCountyLst[0][1]
        elif cand[2] == "REP":
            candRep = cityByCandidateCountyLst[1][1]
        elif cand[2] == "LIB":
            candLib = cityByCandidateCountyLst[2][1]
        
    return candDem, candRep, candLib

'''
=======================================================
createCountyList Function
=======================================================
This function creates a single dimensional list
with all the counties in Massachusetts. It return the
new list back to the main function.
=======================================================
'''
def createCountyLst(cityCountyList):
    '''
    This function creates a new list named counties, then uses list comprehension to append each county from cityCountyList to the new list if it has not 
    already been added to prevent duplicate values from being added to counties. This new list is then returned to the main() function. 
    '''
    
    counties = []
    [counties.append(row[1]) for row in cityCountyList if row[1] not in counties]
    
    return counties

'''
==============================================================
calculateVotesCountyCandidate Function
==============================================================
This function takes the data in the votesByCandidateCountyLst
list which has the cities replaced with counties
and creates a new multi-dimensional list that contains
the county x totals for the 3 candidates that ran
for governor in Massachusetts (Dem. Rep, Lib). Returns
the new list to the main function.
==============================================================
'''
def calculateVotesCountyCandidate(votesByCandidateCountyLst, cityCountyLst, candDem, candRep, candLib):
    '''
    Here, a call to the createCountyLst() function is made, which returns a list containing the name of each county. It is then sorted in alphabetical order. A 
    new multidimensional list named votesCountyCandidate is made, which will store the county, candidate name, number of votes, and party information for each candidate. 
    '''
    
    counties = createCountyLst(cityCountyLst)
    counties.sort()
    votesCountyCandidate = []
    
    '''
    The nested for loops here cycle through each county, and within each county a second for loop cycles through the data in votesByCandidateCountyLst. A nested 
    if statement first checks if the county name in the counties list matches the county name in votesByCandidateCountyLst. If it does, a second if statement checks
    if the candidate name matches the one stored in votesByCandidateCountyLst; if it does, the votes stored in votesByCandidateCountyLst is added to a variable that
    counts the number of votes for each candidate in the county currently being checked. After the if statement is executed, a list for each party is created that 
    stores the county, candidate name, total votes in the county being checked, and their party. These lists are then all appended to the votesCountyCandidate. The
    county for loop then cycles to the next county being checked, and resets the vote counters to zero. After the for loop has gone through each county, the
    votesCountyCandidate is returned to the main() function.
    '''
    
    for county in counties:
        demVotes = 0
        repVotes = 0
        libVotes = 0
        for x in votesByCandidateCountyLst:
            if county == x[0]:
                if candDem == x[1]:
                    demVotes += int(x[3])
                elif candRep == x[1]:
                    repVotes += int(x[3])
                elif candLib == x[1]:
                    libVotes += int(x[3])
        countyDem = [county, candDem, demVotes, votesByCandidateCountyLst[0][2]]
        countyRep = [county, candRep, repVotes, votesByCandidateCountyLst[1][2]]
        countyLib = [county, candLib, libVotes, votesByCandidateCountyLst[2][2]]
        votesCountyCandidate.append(countyDem)
        votesCountyCandidate.append(countyRep)
        votesCountyCandidate.append(countyLib)
    return votesCountyCandidate

'''
=============================================================================================================
printCountyResults Function
=============================================================================================================
This function takes the list that contains the total votes
by county and candidate and prints out the results in the following format:
Example: 
Barnstable DEM: Maura Healey  70,163 59.1% REP: Geoff Diehl  46,011 38.8% LIB: Kevin Reed   1,556  1.3% 
=============================================================================================================
'''
def printCountyResults(totalVotesByCountyLst, countyVoteTotals, STATE):
    '''
    The first block of code here stores the title and subheading information for the county results table in their own variables. The next block then creates the table header
    using f-string formatting. 
    '''
    
    title = f"{STATE} County Results"
    countyTitle = "County"
    cand1Title = "Candidate 1"
    cand2Title = "Candidate 2"
    cand3Title = "Candidate 3"

    print("=" * 135)
    print(f"{title:^135}")
    print("=" * 135)
    print(f"{countyTitle} {cand1Title:^55} {cand2Title:^30} {cand3Title:^50}")
    print("=" * 135)
    
    '''
    The nested for loop here first cycles through the countyVoteTotals list and prints the name of the county being checked. The next for loop then cycles through
    a list containing the names of each candidate, and the third for loop cycles through the information stored in totalVotesByCountyLst. An if statement checks
    if the candidate name in totalVotesByCountyLst matches the name being checked in the candidate for loop. If it does, f-string formatting is used to print out
    the required information. A counter variable, y, is then incremented so the correct number of votes is printed for the next iteration of the for loop. The if
    statement is then broken out of so the same information is not printed out repeatedly. 
    '''
    
    y = 0   
    for county in countyVoteTotals:
        print(f"{county[0]:<15}", end="")
        for candidate in ["Maura Healey", "Geoff Diehl", "Kevin Reed"]:
            for x in totalVotesByCountyLst:
                if x[1] == candidate:
                    print(f"{x[3]}:  {x[1]} {totalVotesByCountyLst[y][2]:>9,}{ (totalVotesByCountyLst[y][2] / int(county[1])) * 100:>7.1f}%       ", end="")
                    y += 1
                    break
            
        print()
    print("=" * 135)
    print()
'''
=============================================================================
printOverallResults Function
=============================================================================
This function calculates the total votes from all Massachusetts counties
for each candidate and prints out the final results of the governor election
in the following format:
==================================================
           Massachusetts State Results            
==================================================
Democrat   : Maura Healey   1,584,403 63.09% WON
Republican : Geoff Diehl      859,343 34.22%
Libertarian: Kevin Reed        39,244  1.56%
=============================================================================
'''
def printOverallResults(candidateCountyVotesLst, totalStateVote, demCan, repCan, libCan, state):
    '''
    The first block of code here stores the title and subheading information for the state results table in their own variables. The next block then creates the table header
    using f-string formatting. 
    '''
    
    title = f"{state} State Results"
    subHead1 = "Party"
    subHead2 = "Candidate"
    subHead3 = "Votes"
    subHead4 = "%"
    
    print("=" * 54)
    print(f"{title:^54}")
    print("=" * 54)
    print(f"{subHead1} {subHead2:^27} {subHead3} {subHead4:>5}")
    print("=" * 54)

    '''
    The for loop below uses a slightly modified version of the for loop used to calculate the total number of votes by county, with the main difference being that
    the vote counters are stored outside the for loop so a cumulative total is reached. A list named stateResultsLst is created that stores the party name, candidate
    name, and total votes for each candidate, and the highest number of votes is stored by using max() to grab the largest vote number from a list comprehension
    that stores the number of votes for each candidate. 
    '''
    
    demVotesTotal = 0
    repVotesTotal = 0
    libVotesTotal = 0
    for x in candidateCountyVotesLst:
        if demCan == x[1]:
            demVotesTotal += int(x[2])
        elif repCan == x[1]:
            repVotesTotal += int(x[2])
        elif libCan == x[1]:
            libVotesTotal += int(x[2])
            
    stateResultsLst = [["Democrat", demCan, demVotesTotal], ["Republican", repCan, repVotesTotal], ["Libertarian", libCan, libVotesTotal]]
    mostVotes = max([y[2] for y in stateResultsLst])

    '''
    The for loop here cycles through stateResultsLst and prints out the required information using f-string formatting. An if statement is included to print "WON"
    next to the candidate that won the election.
    '''
    
    for y in stateResultsLst:
        print(f"{y[0]:<11}:   {y[1]:<13} {y[2]:>10,}   {(y[2] / totalStateVote) * 100:>5.2f}% ", "WON" if y[2] == mostVotes else "") 
    print("=" * 54)
                 
'''
================================================
Main Function
================================================
Used to drive the program and makes calls
to the function to perform the required
tasks to meet the assignment 3 requirements.
================================================   
'''
def main():
    STATE = 'Massachusetts'  # Constant: Name of state, used in the result outputs
    STATE_TOTAL_VOTES = 2511461  # Constant: Total votes cast in the general election for governor

    '''
    ************************************
    Read data from the 3 files.
    ************************************
    '''
    votesByCandidateCityLst, cityCountyLst, countyVoteTotals = processDataFiles()
    del votesByCandidateCityLst[0]  # remove list element 0 (Header)
    del cityCountyLst[0]          # remove list element 0 (Header)
    del countyVoteTotals[0]        # remove list element 0 (Header)

    # print(votesCandidateCityList)
    # print(cityCountyList)
    # print(countyVoteTotals)

    '''
    **********************************
    Replace the city with the county
    that the city belongs to.
    **********************************
    '''
    votesByCandidateCountyLst = convertCityToCounty(votesByCandidateCityLst, cityCountyLst)
    del votesByCandidateCityLst  # delete the votesCandidateCityList from memory
    # print(votesCandidateCountyList)

    '''
    ********************************************
    Get the candidates that ran for governor
    ********************************************
    '''
    candDem, candRep, candLib = getCandidates(votesByCandidateCountyLst)
    #print(candDem)
    #print(candRep)
    #print(candLib)

    '''
    *******************************************
    Create a new list that contains the
    total votes that each candidate received
    from each county.
    *******************************************
    '''
    totalVotesByCountyLst = calculateVotesCountyCandidate(votesByCandidateCountyLst, cityCountyLst, candDem, candRep, candLib)
    # print(totalVotesByCountyLst)

    '''
    *************************************
    Print out the county results
    *************************************
    '''
    printCountyResults(totalVotesByCountyLst, countyVoteTotals, STATE)

    '''
    *************************************************
    Print out the final governor election results
    *************************************************
    '''
    printOverallResults(totalVotesByCountyLst, STATE_TOTAL_VOTES, candDem, candRep, candLib, STATE)


main()  # Call to the main function