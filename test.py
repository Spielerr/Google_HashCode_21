sim_dur, num_inter, num_str, num_cars, bonus = tuple(map(int, input().split()))

streets = {}

for i in range(num_str):
	l = input().split()
	streets[l[2]] = []
	streets[l[2]].extend([int(l[0]), int(l[1]), int(l[3])]) # start end duration_on_street(L) occurences

cars = {}
for i in range(num_cars):
	l = input().split()
	cars[i] = []
	cars[i].extend(l)

# print(streets)
# print(cars)

intersection = {}

for k in streets:
	try:
		intersection[streets[k][1]].append(k)
	except:
		intersection[streets[k][1]] = [k]
# print(intersection)

for k in cars:
	for i in cars[k][1::]:
		# print(i)
		try:
			streets[i][3] += 1
		except:
			streets[i].append(1)
# print(streets)

T_scores = {}
T_sum = 0
for k in streets:
	try:
		T_scores[k] = streets[k][3] / streets[k][2]
	except:
		T_scores[k] = 0
	# T_sum += T_scores[k]
# print(T_scores)
to_print = {}
for k in intersection:
# 	T_scores[k] = T_scores[k] / T_sum
	for i in intersection[k]:
		T_sum += T_scores[i]
	for i in intersection[k]:
		try:
			T_scores[i] = T_scores[i] / T_sum
			to_print[k] = 1
		except:
			to_print[k] = 0
	T_sum = 0

for i in T_scores:
	T_scores[i] = int(T_scores[i] * 0.05 * sim_dur)

# print(T_scores)
# print(to_print)
t_count = 0
for i in to_print:
	if(to_print[i]):
		t_count += 1
print(t_count)
for i in intersection:
	if(to_print[i]):
		print(i)
		count = 0
		for j in intersection[i]:
			if(T_scores[j]):
				count += 1
		if(count):
			print(count)
			for j in intersection[i]:
				if(T_scores[j]):
					print(j, T_scores[j])


