import csv
csvpath = "Starter_Code/PyPoll/Resources/election_data.csv"
candidates = []
candidate_count = 0
vote_count = 0
stockham_precentage = 0
DeGette_percentage = 0
Doane_percentage = 0
candidate1 = 'Charles Casper Stockham'
candidate1_count = float(0)

candidate2 = 'Diana DeGette'
candidate2_count = float(0)

candidate3 = 'Raymon Anthony Doane'
candidate3_count = float(0)


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    next_row = next(csvreader)

    voter_count = 0
    # The total number of votes cast
    for row in csvreader:
        current_candidate = row[2]
        if current_candidate not in candidates:
            candidates.append(current_candidate)
        voter_count = voter_count + 1

        if  candidate1 == row [2]:
            
            candidate1_count += 1
        elif candidate2 == row[2]:
            candidate2_count += 1
        elif candidate3 == row[2]:
            candidate3_count += 1
        
    candidate_total = candidate1_count + candidate2_count + candidate3_count
    
    candidate1_perc = candidate1_count/candidate_total
    candidate2_perc = candidate2_count/candidate_total
    candidate3_perc = candidate3_count/candidate_total

    

        

        
    print("Total Votes:", voter_count)
    print("Charles Casper Stockham",candidate1_count, candidate1_perc)
    print("Diana DeGette", candidate2_count, candidate2_perc) 
    print("Raymon Anthony", candidate3_count, candidate3_perc)
    
    if (candidate1_count > candidate2_count) and (candidate1_count > candidate3_count):
        print("Charles Casper Stockham is the winner")
        
    elif candidate2_count > candidate3_count:
         print("Diana DeGette is the winner")
    elif candidate3_count > candidate2_count:
        print ("Raymon Anthony is the winner")
    # A complete list of candidates who received votes
    


   



