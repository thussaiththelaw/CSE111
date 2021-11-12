from sentences import get_determiner, get_noun, get_verb, get_preposition
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    #1. test the single nouns
    single_nouns = ['adult', 'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'woman']

    #this loop will repeat the statement inside it 20 times
    for _ in range(20):
        noun = get_noun(1)

        #verify that the noun returned from get_noun is one of the nouns in single_nouns list
        assert noun in single_nouns
    

    #2. test the plural nouns
    plural_nouns = ['adults', 'birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'women']

    #this loop will repeat the statements inside it 20 times
    for _ in range(20):
        noun = get_noun(2)

        #verify that the noun returned from get_noun is one of the nouns in plural_nouns list
        assert noun in plural_nouns


def test_get_verb():
    #1. test the past tense verbs

    past_tense_verbs = ["drank", "ate", "grew", "laughed", 
        "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    #this loop will repeat the statement inside it 20 times
    for _ in range(20):
        verb = get_verb(1, "past")

        #verify that the verb returned from get_noun is one of the verbs in plural_nouns list
        assert verb in past_tense_verbs
    
    #2. test the singular present tense verbs
    singular_present_tense_verbs = ["drinks", "eats", "grows", "laughs", 
        "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    
    #this loop will repeat the statement inside it 20 times
    for _ in range(20):
        verb = get_verb(1, "present")

        #verify that the verb returned from get_verb is one of the verbs in singular_present_tense_verbs list
        assert verb in singular_present_tense_verbs

    #3. test the plural present tense verbs
    plural_present_tense_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    #this loop will repeat the statment inside it 20 times
    for _ in range(20):
        verb = get_verb(2, "present")

        #verify that the verb returned from get_verb is one of the verbs in plural_present_tense_verbs list
        assert verb in plural_present_tense_verbs

    #4. test future tense verbs
    future_tense_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    #this loop will repeat the statement inside it 20 times
    for _ in range(20):
        verb = get_verb(1, "future")

        #verify that the verb returned from get_verb is one of the verbs in future_tense_verbs list
        assert verb in future_tense_verbs


def test_get_preposition():
    preposition_list = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    #this loop will repeat the statement inside it 40 times
    for i in range(40):
        preposition = get_preposition()

        #verify that the preposition returned from get_preposition is one of the prepositions in preposition_list
        assert preposition in preposition_list

pytest.main(["-v", "--tb=line", "-rN", __file__])