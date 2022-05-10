import requests
import requests.compat as rc

uri = 'https://opendomesday.org/api/1.0/place/'


def get_manors(place_id):
    r = requests.get(rc.urljoin(uri, str(place_id)))
    place_info = r.json()
    manor_ids = [m['id'] for m in place_info['manors']]
    return manor_ids

if __name__ == '__main__':
    print(get_manors(1036))

