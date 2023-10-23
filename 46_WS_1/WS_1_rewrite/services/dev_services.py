from data.database import query_count


def dev_id_exists(id: int):
    return query_count('SELECT COUNT(*) from devs WHERE id = ?',
                       (id,)) > 0