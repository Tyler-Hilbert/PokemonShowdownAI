import csv

movesDict = {}
with open('12_30_18Gen4Movepool.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: # Column names
            line_count += 1
        else: # Pokemon data
            name = row[0]
            moves = []
            for move in row[1:]:
            	if move != "":
            		moves.append(move.strip())
            
            movesDict[name] = moves
            
            line_count += 1
            
for pkmnName in movesDict:
	print (pkmnName)
	print (movesDict[pkmnName])
	print ("\n")