
import requests
import re

pattern_response = re.compile(r'\s+|\[|\]')
pattern_null     = re.compile(r'null')


def confirm_source_exist(isbn_13):

    if isbn_13 == '':
        return False

    # f_stringが使えるようになるのはpython 3.6以降
    # url = f'https://api.openbd.jp/v1/get?isbn={isbn_13}&pretty'
    url = 'https://api.openbd.jp/v1/get?isbn={isbn}&pretty'.format(isbn=isbn_13)

    r = requests.get(url)
    # print(response.text)
    response = ''.join(r.text.split('\n'))

    if pattern_null.match(pattern_response.sub('', response)):
        return False

    json_data = r.json()
    openbd_dict = json_data[0]

    if 'summary' not in openbd_dict.keys():
        return False
    elif 'cover' not in openbd_dict['summary'].keys():
        return False
    else:
        return openbd_dict['summary']['cover']


# ISBN10をISBN13に変換する
def isbn10_to_13(isbn_10):

    isbn_10_without_hyphen = ''.join(isbn_10.split('-'))
    # f_stringが使えるようになるのはpython 3.6以降
    # temp = f'978{isbn_10_without_hyphen[0:-1]}'  # 末尾はチェックディジットなので省く
    temp = '978{isbn}'.format(isbn=isbn_10_without_hyphen[0:-1])  # 末尾はチェックディジットなので省く
    total = 0
    for i in range(len(temp)):
        if not i % 2:  # Even
            total += int(temp[i]) * 1
        else:  # Odd
            total += int(temp[i]) * 3

    if total % 10:
        check_digit = 10 - (total % 10)
    else:
        check_digit = 0

    isbn_13 = temp + str(check_digit)

    return isbn_13


