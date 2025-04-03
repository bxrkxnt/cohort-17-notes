from stwars import get_stwars

def test_get_stwars(requests_mock):
    requests_mock.get("https://swapi.dev/api/planets", json={})
    response = get_stwars("planets")

    assert requests_mock.called
    assert requests_mock.call_count == 1
    assert requests_mock.last_request.method == "GET"
    assert isinstance(response, dict)