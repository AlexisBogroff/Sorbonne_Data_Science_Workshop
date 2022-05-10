import json

import pandas as pd
import requests
import requests.compat as rc

target = 'Derbyshire'
uri_c = 'https://opendomesday.org/api/1.0/county/'
uri_p = 'https://opendomesday.org/api/1.0/place/'
uri_m = 'https://opendomesday.org/api/1.0/manor/'


def get_place_ids():
    r = requests.get(uri_c)
    counties = r.json()
    county_info = next(c for c in counties if c['name'] == target)
    place_ids = [p['id'] for p in county_info['places_in_county']]
    return place_ids


def get_manor_ids(place_id):
    r = requests.get(rc.urljoin(uri_p, str(place_id)))
    place_info = r.json()
    manor_ids = [m['id'] for m in place_info['manors']]
    return manor_ids


def get_all_manor_ids(place_ids):
    all_manor_ids = set()
    for place_id in place_ids:
        all_manor_ids.update(get_manor_ids(place_id))
    return all_manor_ids


def get_manor_infos(manor_id):
    r = requests.get(rc.urljoin(uri_m, str(manor_id)))
    manor_info = r.json()
    geld = manor_info['geld']
    totalploughs = manor_info['totalploughs']
    return geld, totalploughs


def get_all_manor_infos(manor_ids):
    manor_infos = []
    for each_manor_id in manor_ids:
        geld, totalploughs = get_manor_infos(each_manor_id)
        manor_infos.append([each_manor_id, geld, totalploughs])
    return manor_infos


if __name__ == '__main__':
    place_ids = get_place_ids()
    with open('place_ids.json', 'w+') as f:
        json.dump(place_ids, f)
    all_manor_ids = get_all_manor_ids(place_ids)
    with open('all_manor_ids.json', 'w+') as f:
        json.dump(list(all_manor_ids), f)
    all_manor_infos = get_all_manor_infos(all_manor_ids)
    with open('all_manor_infos.json', 'w+') as f:
        json.dump(all_manor_infos, f)
    df_all_manor_infos = pd.DataFrame(
        all_manor_infos, columns = ['id', 'geld', 'totalploughs'])
    with open('df_all_manor_infos.json', 'w+') as f:
        json.dump(df_all_manor_infos.to_json(), f)
    print(df_all_manor_infos.sum())
