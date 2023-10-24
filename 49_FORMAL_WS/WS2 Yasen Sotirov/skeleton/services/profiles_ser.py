from data.database import read_query, query_count
from data.models import Profile, Category


def all_profiles(country_code: str | None = None):
    if country_code is None:
        data = read_query('''SELECT id, ip_address, country_code 
                            FROM profiles''')
    else:
        data = read_query('''SELECT id, ip_address, country_code 
                                FROM profiles 
                                WHERE country_code LIKE ?''', (country_code,))

    return (Profile.from_query_result(*row) for row in data)



def get_by_id(id: int):
    return read_query('''SELECT id, ip_address, country_code
                            FROM profiles
                            WHERE id = ?''', (id,))




def profile_exists(id: int):
    return query_count('''SELECT COUNT(*) from profiles WHERE id = ?''',
                       (id,)) > 0


def unique_country_codes():
    data = read_query('''SELECT DISTINCT country_code FROM profiles''')
    return (Profile.country_codes(*row) for row in data)
