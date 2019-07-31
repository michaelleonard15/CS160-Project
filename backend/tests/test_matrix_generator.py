import pprint
import os
import json
import flaskr.matrix_generator as matgen
import pytest

TEST_FILE_PATH = os.getcwd() + "/tests/testdata/matrix_generator/"
## TEST FILE 1: SINGLE SCHOOL ##

@pytest.fixture
def set_ids():
    matgen.__current_id = 0
    matgen.__current_neg_id = -1
    
def test_extract_source_row(set_ids):

    # Opening files
    with open(TEST_FILE_PATH + "test1-db.json") as f:
        test1_db = json.load(f)
    with open(TEST_FILE_PATH + "test1-after-origin.json") as f:
        test1_after_origin = json.load(f)

    ## ROW 1

    # Initialization
    row = test1_db['Sections'][0]['1']
    matrix = [[]]
    src_lookup = []

    # Running
    matgen._extract_source_row(row, matrix, src_lookup)

    # Expected values
    lookup_expected = [{"course": {
        "isSelected": False,
        "courseName": "College Composition",
        "courseID": "ENGL 1A",
        "units": 4,
        "isOrigin": True
      }}]
    matrix_expected = [[{"courses": [[0]], "relationToNext": "AND"}]]

    # Assertions
    assert matrix == matrix_expected
    assert src_lookup == lookup_expected

    ## ROW 2 ##

    row = test1_db['Sections'][0]['2']

    # Running
    matgen._extract_source_row(row, matrix, src_lookup)

    # Expected values

    # Assertions


def test_add_to_lookup(set_ids):

    db_course = {"courseID":"ENGL 1A", "courseName": "College Composition", "units":4}
    lookup = []
    new_id = matgen._add_to_lookup(db_course, lookup, is_origin=True)

    lookup_expected = [
        {"key": 0,
         "course": {
             "isSelected": False,
             "courseName": "College Composition",
             "courseID": "ENGL 1A",
             "units": 4,
             "isOrigin": True}}]
    
    assert lookup == lookup_expected
    assert new_id == 0

def test_add_to_lookup_duplicates(set_ids):

    course1 = {"courseID":"ENGL 1A", "courseName": "College Composition", "units":4}
    course2 = {"courseID":"ENGL 1A", "courseName": "College Composition", "units":4}
    lookup = []

    lookup_expected = [
    {"key": 0,
        "course": {
            "isSelected": False,
            "courseName": "College Composition",
            "courseID": "ENGL 1A",
            "units": 4,
            "isOrigin": True}}]
    
    new_id = matgen._add_to_lookup(course1, lookup, is_origin=True)

    assert lookup == lookup_expected
    assert new_id == 0

    new_id = matgen._add_to_lookup(course2, lookup, is_origin=True)

    assert lookup == lookup_expected
    assert new_id == 0