from main import get_anime_data

def test_get_anime_data(requests_mock):
    response = requests_mock.get("https://api.jikan.moe/v4/anime?&limit=100&q=test&sfw", json={})

    get_anime_data("https://api.jikan.moe/v4/anime?&limit=100&q=test&sfw")
    assert response.called
    assert response.called_once
    assert response.call_count == 1