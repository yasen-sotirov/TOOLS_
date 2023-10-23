from data.database import read_query
from data.models import Profile


def all_profiles(country_code: str | None = None):
    if country_code is None:
        data = read_query('SELECT id, ip_address, country_code'
                          'FROM profiles')
    else:
        data = read_query('SELECT id, ip_address, country_code'
                          'FROM profiles'
                          'WHERE country_code LIKE ?', (country_code,))

    return (Profile.from_query_result(*row) for row in data)












