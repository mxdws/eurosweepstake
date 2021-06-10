# Sweepstake
# ----------

import random, json
from time import sleep

teams = [
	'Turkey', 'Italy', 'Wales', 'Switzerland',
	'Denmark', 'Finland', 'Belgium', 'Russia',
	'Netherlands', 'Ukraine', 'Austria', 'North Macedonia',
	'England', 'Croatia', 'Scotland', 'Czech Republic',
	'Spain', 'Sweden', 'Poland', 'Slovakia',
	'Hungary', 'Portugal', 'France', 'Germany'
]

names = [
	'Billy',
	'Billy',
	'Anabelle',
	'Anabelle',
	'Evie',
	'Evie',
	'Livvy',
	'Livvy',
	'Dylan',
	'Dylan',
	'Amy',
	'Amy',
	'Alfie',
	'Alfie',
	'Ted',
	'Martin',
	'Steve',
	'Anna',
	'Nene',
	'Dave',
	'Claire',
	'Simon',
	'Tammy',
	'Gary'
]

print('Number of People: ' + str(len(names)))
print('Number of Teams: ' + str(len(teams)))

print('Shuffling Names...')
# sleep(3)
random.shuffle(teams)
print('Shuffling Teams...')
# sleep(3)
random.shuffle(names)
print('Done! Ready to begin...')
# input()

sstake = zip(teams,names)

sweepResult =[]
count = 0
for (t,n) in sstake:
	count += 1
	nextCount = count + 1
	# print(n, end="")
	# sleep(1)
	# print("...", end="")
	# input()
	# print(t)
	# input()
	
	result = {
		"drawPosition": str(count),
		"nextPosition": str(nextCount),
		"name": n,
		"team": t,
        "status": "Active"
	}
	
	sweepResult.append(result)
	

	
print('\nSweepstake Complete!')

with open('./sweepstake.json', 'w') as f:
	json.dump(sweepResult,f)
