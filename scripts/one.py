f = open('input\input_one.txt', 'r')
input = f.readlines()

one = []
two = []

for line in input:
    line_arr = line.split()
    one.append(line_arr[0])
    two.append(line_arr[1])

one = sorted(one)
two = sorted(two)

diff_sum = 0

for i in range(len(one)):
    diff_sum += abs(int(one[i]) - int(two[i]))


print("The total difference is {}".format(diff_sum))

similarity_score = 0

for i in range(len(one)):
    current_num = int(one[i])
    count = 0
    for j in range(len(two)):
        if int(two[j]) == current_num:
            count += 1

    similarity_score += current_num * count

print("Similarity score: {}".format(similarity_score))

    

