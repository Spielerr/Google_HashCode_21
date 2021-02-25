sim_dur, num_inter, num_str, num_cars, bonus = tuple(map(int, input().split()))
import math
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
#{'rue-de-londres': [2, 0, 1], 'rue-d-amsterdam': [0, 1, 1], 'rue-d-athenes': [3, 1, 1], 'rue-de-rome': [2, 3, 2], 'rue-de-moscou': [1, 2, 3]}


# {0: ['4', 'rue-de-londres', 'rue-d-amsterdam', 'rue-de-moscou', 'rue-de-rome'], 1: ['3', 'rue-d-athenes', 'rue-de-moscou', 'rue-de-londres']}
# print(cars)

intersection = {}

for k in streets:
	try:
		intersection[streets[k][1]].append(k)
	except:
		intersection[streets[k][1]] = [k]

#print(intersection)
#{0: ['rue-de-londres'], 1: ['rue-d-amsterdam', 'rue-d-athenes'], 3: ['rue-de-rome'], 2: ['rue-de-moscou']}

for k in cars:
	for i in cars[k][1::]:
		# print(i)
		try:
			streets[i][3] += 1
		except:
			streets[i].append(1)
# print(streets)

T_scores = {}

for j in intersection:
	for k in intersection[j]:
		T_scores[(j,k)] = 0

# print(T_scores)

total_l_each_car = {}
for i in cars:
	car_l = 0
	for k in cars[i][2::]:
		# print(k)

		car_l += streets[k][2]

	total_l_each_car[i] = 1/car_l

# print(total_l_each_car)


for i in cars:
	for k in cars[i][1::]:
		for j in intersection:
			if k in intersection[j]:
				try:
					T_scores[(j,k)] += total_l_each_car[i]
				except:
					T_scores[(j,k)]  = 0


# print(T_scores)
for i in T_scores:
	# print(i)
	T_scores[i] = math.ceil(T_scores[i] * 0.005 * sim_dur)

to_print = {}
for i in intersection:
	to_print[i] = 0
for i in T_scores:
	if T_scores[i]:
		to_print[i[0]] = 1
t_count = 0
for i in to_print:
	if(to_print[i]):
		t_count += 1
print(t_count)






for i in intersection:
	if(to_print[i]):
		print(i)

		print(len(intersection[i]))

		for j in intersection[i]:
			print(j, T_scores[(i, j)])


