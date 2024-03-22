def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    # Calculate the probability of not A
    prior_not_a = 1 - prior_a

    # Calculate the probability of B given not A
    conditional_b_given_not_a = 1 - conditional_b_given_a

    # Calculate the total probability of B
    p_b = (conditional_b_given_a * prior_a) + (conditional_b_given_not_a * prior_not_a)

    # Calculate the probability of A given B using Bayes' theorem
    p_a_given_b = (conditional_b_given_a * prior_a) / p_b

    return p_a_given_b


prior_a = float(input("Enter the prior probability of event A: "))
prior_b = float(input("Enter the prior probability of event B: "))
conditional_b_given_a = float(input("Enter the conditional probability of B given A: "))

# Calculate and print the result
print(bayes_theorem(prior_a, prior_b, conditional_b_given_a))
