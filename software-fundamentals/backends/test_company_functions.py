from company_functions import is_valid_company

def test_is_valid_company_rejects_missing_keys():

    result = is_valid_company({})

    assert not result