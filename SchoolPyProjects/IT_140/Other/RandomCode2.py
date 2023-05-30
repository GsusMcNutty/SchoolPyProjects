user_score = 0
simon_pattern = input()
user_pattern = input()

for count, i in enumerate(user_pattern):
    if i != simon_pattern[count]:
        break
    user_score += 1

print('User score:', user_score)
