import os
import csv
#open csv path
with open('Resources/election_data.csv', newline= '') as file:
        csv_reader=csv.reader(file, delimiter=',')
        header=next(csv_reader)
#create variables    
        candidate_list = []
        total_votes = 0
#create for loop and count votes
        for row in csv_reader:
            total_votes += 1
            candidate_list.append(row[2])
#candidate vote count 
Khan_votes = int(candidate_list.count('Khan'))
Correy_votes = int(candidate_list.count('Correy'))
Li_votes = int(candidate_list.count('Li'))
O_Tooley_votes = int(candidate_list.count("O'Tooley")) 
#candidate percent votes
Khan_percentage = Khan_votes * 100 / total_votes
Correy_percentage = Correy_votes * 100 / total_votes
Li_percentage = Li_votes * 100 / total_votes
O_Tooley_percentage = O_Tooley_votes * 100 / total_votes
#declair winner
Final_votes = [Khan_votes, Correy_votes, Li_votes, O_Tooley_votes]
winner = max(Final_votes)
#print results
lines = '--------------------'
print('Election Results')
print(lines)
print(f'Total Votes: {total_votes}')
print(lines)
print(f'Khan: {Khan_percentage}% ({Khan_votes})')
print(f'Correy: {Correy_percentage}% ({Correy_votes})')
print(f'Li: {Li_percentage}% ({Li_votes})')
print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley_votes})")
print(lines)
print(winner)
#export text file
with open('Output.txt', 'w') as text_file:
    text_file.write('\nElection Results')
    text_file.write('\n' + lines)
    text_file.write(f'\nTotal Votes: {total_votes}')
    text_file.write('\n' + lines)
    text_file.write(f'\nKhan: {Khan_percentage}% ({Khan_votes})')
    text_file.write(f'\nCorrey: {Correy_percentage}% ({Correy_votes})')
    text_file.write(f'\nLi: {Li_percentage}% ({Li_votes})')
    text_file.write(f"\nO'Tooley: {O_Tooley_percentage}% ({O_Tooley_votes})")
    text_file.write('\n' + lines)
    text_file.write(f'\nWinner: {winner}' )
    text_file.write('\n' + lines)

    

    

    



    

            
            




            

