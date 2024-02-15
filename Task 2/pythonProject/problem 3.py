# Input processing
n = int(input())
scores = list(map(int, input().split()))


sorted_scores = sorted(scores, reverse=True)


runner_up_score = None
for score in sorted_scores:
    if score < max(sorted_scores):
        runner_up_score = score
        break


print(runner_up_score)



