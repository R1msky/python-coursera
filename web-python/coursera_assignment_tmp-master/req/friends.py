import requests

from datetime import datetime
from operator import itemgetter


def calc_age(uid):
    uid_response = requests.get('https://api.vk.com/method/users.get', params={
        'access_token': '0206ca850206ca850206ca851a0273419e002060206ca855dda611678169ad8feb9a478', 'v': 5.71,
        'user_ids': uid}).json()

    user_id = (uid_response['response'][0]['id'])
    friends = requests.get('https://api.vk.com/method/friends.get', params={
        'access_token': '0206ca850206ca850206ca851a0273419e002060206ca855dda611678169ad8feb9a478', 'v': 5.71,
        'user_id': user_id, 'fields': 'bdate'}).json()

    ages = []
    ages_set = set()
    ages_dist = []
    for friend in friends['response']['items']:
        if 'bdate' in friend:
            bdate = friend['bdate']
            if len(bdate) > 6:
                year = str(bdate).split('.')
                age = datetime.today().year - int(year[2])
                ages.append(age)
                ages_set.add(age)

    for age in ages_set:
        ages_dist.append((age, ages.count(age)))

    ages_dist = sorted(ages_dist, key=itemgetter(0))
    ages_dist = sorted(ages_dist, key=itemgetter(1), reverse=True)
    return ages_dist


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
