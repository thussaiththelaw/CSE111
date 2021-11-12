from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    #"""Return a string in this form "family_name; given_name".
    #For example, if this function were called like this:
    #make_full_name("Sally", "Brown"), it would return "Brown; Sally".
    #"""
    assert make_full_name("Sally", "Brown") == "Brown;Sally" 
    assert make_full_name(" ", "Smith") == "Smith; "
    assert make_full_name("Santino", " ") == " ;Santino"
    
def test_extract_family_name():
    # """Extract and return the family name from a
    # string in this form "family_name; given_name".
    # For example, if this function were called like this:
    # extract_family_name("Brown; Sally"), it would return "Brown".
    # """
    assert extract_family_name("; ") == ""
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("; Cedrick") == ""
    assert extract_family_name("Law; The") == "Law"
    assert extract_family_name("bojangle; ") == "bojangle"
    assert extract_family_name("Washington; Jorge") == "Washington"


def test_extract_given_name():
    #"""Extract and return the given name from a
    #string in this form "family_name; given_name".
    #For example, if this function were called like this:
    #extract_given_name("Brown; Sally"), it would return "Sally".
    #"""
    assert extract_given_name("Brown/ Sally") == "Sally"
    assert extract_given_name("/ ") == ""
    assert extract_given_name("bojangle/ ") == ""
    assert extract_given_name("/ My Mom!") == "My Mom!"
    

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])