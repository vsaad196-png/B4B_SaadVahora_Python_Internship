#You are given a list of tuples where each tuple has a student name and their marks, for example [("Riya", 88), ("Aman", 95), ("Sara", 72)]. Sort this list so that the topper appears first, using the key parameter of sort() or sorted().
scores = [("Riya", 88), ("Aman", 95), ("Sara", 72)]

scores.sort(key=lambda item: item[1])
print(scores)

top_scorer_first = sorted(scores, key=lambda item: item[1], reverse=True)
print(top_scorer_first)

