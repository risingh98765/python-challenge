import os 
import csv

csvpath = os.path.join('Resources','election_data.csv')

total_votes = 0
candidates = []
khan_count = 0 
khan_percentage = 0
correy_count = 0
correy_percentage = 0 
li_count = 0
li_percentage = 0
tooley_count = 0
tooley_percentage = 0 

j = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)

    
    for row in csvreader:
        j.append(row[2])
        if row[2] == 'Khan':
            khan_count += 1
        elif row[2] == 'Correy':
            correy_count += 1
        elif row[2] == 'Li':
            li_count += 1 
        else:
            tooley_count += 1 
    total_votes = khan_count + correy_count + li_count + tooley_count 

    for x in j: 
        if x not in candidates:
            candidates.append(x)
    
    khan_percentage = khan_count/total_votes *100
    correy_percentage = correy_count/total_votes*100
    li_percentage = li_count/total_votes*100
    tooley_percentage = tooley_count/total_votes*100

filepath = os.path.join('Analysis','election_results.txt')
with open(filepath,'w') as text:
    text.write(f'Election Results')
    text.write(f'/n')
    text.write(f'----------------------------------------------------------')
    text.write(f'/n')
    text.write(f'Total Votes: {total_votes}')
    text.write(f'/n')
    text.write(f'-----------------------------------------------------------')
    text.write(f'/n')
    text.write(f'Khan: {khan_percentage}% ({khan_count})')
    text.write(f'/n')
    text.write(f'Correy: {correy_percentage}% ({correy_count})')
    text.write(f'/n')
    text.write(f'Li: {li_percentage}% ({li_count})')
    text.write(f'/n')
    text.write(f'OTooley: {tooley_percentage}% ({tooley_count})')
    text.write(f'/n')
    text.write(f'-----------------------------------------------------------')
    text.write(f'/n')
    text.write(f'Winner: Khan')
    


print(f'Election Results')
print(f'----------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'-----------------------------------------------------------')
print(f'Khan: {khan_percentage}% ({khan_count})')
print(f'Correy: {correy_percentage}% ({correy_count})')
print(f'Li: {li_percentage}% ({li_count})')
print(f'OTooley: {tooley_percentage}% ({tooley_count})')
print(f'-----------------------------------------------------------')
print(f'Winner: Khan')


