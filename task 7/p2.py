def conditional_probability(event_a, event_b):  #بعد ما استوعبت ان ال الليست دي عباره عن عدد مرات حدوث الحدث مش سامبل
# Count occurrences of both A and B
  count_a_and_b=0 #( a intersect b)
  for i in range(len(event_a)):
      if event_a[i] == 1 and event_b[i] == 1:
          count_a_and_b+=1

# Count occurrences of event A
  count_a = sum(event_a)
# Calculate conditional probability
  if count_a == 0:
    return 0  # Return 0 if event A never occurs
  else:
    return count_a_and_b / count_a  #p(b/a)=p(b intersect a)/p(a)


# Test input
event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]

# Calculate and print conditional probability
print(conditional_probability(event_a, event_b))
