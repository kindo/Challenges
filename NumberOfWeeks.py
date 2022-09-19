def numberOfWeeks(self, milestones):
	if len(milestones) == 1:
		return 1
	
	milestones.sort()
	count = 0

	minVal = milestones[0]
	

	for i in range(len(milestones)-2, -1, -1):
		if milestones[-1] < milestones[i]:

			milestones[-1], milestones[i] = milestones[i], milestones[-1]


	 
		count += 2 * (milestones[i] - minVal)
		milestones[-1] -= (milestones[i] - minVal)
		milestones[i] = minVal
		
	if milestones[-1] == minVal:
		count += sum(milestones)

	elif sum(milestones[:-1]) < milestones[-1]:
		count += 2*sum(milestones[:-1]) + 1

	elif sum(milestones[:-1]) > milestones[-1]:
		count += sum(milestones)
	elif sum(milestones[:-1]) == milestones[-1]:
		count += 2 * milestones[-1]

	return count