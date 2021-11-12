# takes the positive question answers and add the value of the answers to positive_score
def score_positive(q_1, q_2, q_4, q_6, q_7): 
# (numbers 1, 2, 4, 6, 7)
    positive_questions = [q_1, q_2, q_4, q_6, q_7]
    positive_score = 0
    for questions in positive_questions:
        if questions == "D":
            positive_score += 0
        elif questions == "d":
            positive_score += 1
        elif questions == "a":
            positive_score += 2
        elif questions == "A":
            positive_score += 3
#return positive_score to the total score function
    return positive_score

# takes the negative question answers and adds the value of the answers to negative_score
def score_negative(q_3, q_5, q_8, q_9, q_10):
# (numbers 3, 5, 8, 9, 10)
    negative_questions = [q_3, q_5, q_8, q_9, q_10]
    negative_score = 0
    for questions in negative_questions:
        if questions == "D":
            negative_score += 3
        elif questions == "d":
            negative_score += 2
        elif questions == "a":
            negative_score += 1
        elif questions == "A":
            negative_score += 0
# returns negative_score to the total_score function
    return negative_score

#calls the positivity_score and negativity_score functions and adds the returned values
def total_score(q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10):
    positivity_score = score_positive(q_1, q_2, q_4, q_6, q_7)
    negativity_score = score_negative(q_3, q_5, q_8, q_9, q_10)
    total_score = positivity_score + negativity_score
    #return the total score to main
    return (total_score)

def main(): 
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print(" ")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    
    #questions
    q_1 = input("I feel that I am a person of worth, at least on an equal plane with others.: ")
    q_2 = input("I feel that I have a number of good qualities.: ")
    q_3 = input("All in all, I am inclined to feel that I am a failure.: ")
    q_4 = input("I am able to do things as well as most other people.: ")
    q_5 = input("I feel I do not have much to be proud of.: ")
    q_6 = input("I take a positive attitude toward myself.: ")
    q_7 = input("On the whole, I am satisfied with myself.: ")
    q_8 = input("I wish I could have more respect for myself.: ")
    q_9 = input("I certainly feel useless at times.: ")
    q_10 = input("At times I think I am no good at all.: ")
    
    #call total_score to get the results of the test
    t_s = total_score(q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10)
    print(t_s)
    print("A score below 15 may indicate problematic low self-esteem.")

main()