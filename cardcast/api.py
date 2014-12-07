# The MIT License (MIT)
#
# Copyright (c) 2014 bspkrs (bspkrs@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# ADDITIONAL NOTE FROM THE DEVELOPERS OF CARDCASTGAME.COM ON THE USE OF THEIR API
#
# The Cardcast API isn't public, but we (the developers of cardcastgame.com) don't
# have a problem with people tapping into it for small projects.
#
# Our only requirements (right now) are:
#
# A) Make users aware you are using Cardcast decks.
# B) Direct users to our website for any searching/discovery of play codes
#    (i.e., don't roll your own search engine based on our data).
# C) If possible, implement some simple form of caching. The decks aren't immutable
#    (people can edit decks at anytime and the code remains the same), so you
#    shouldn't cache a deck for too long. One popular site caches for 15 minutes.
# D) Use at your own risk! If cardcastgame.com goes down or is hacked or whatever,
#    we (the developers of cardcastgame.com) can't be held liable for any impact on
#    your app. We also reserve the right to revoke access at anytime.

import urllib2, json
from . import constants


# GENERAL METHODS

def get_remote_json(url):
    """Attempts to retrieve a json document from the given URL.

    :type url: str
    :rtype: dict
    """
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    ret = json.loads(r.read())
    if 'id' in ret and ret['id'] == constants.RESOURCE_NOT_FOUND:
        raise Exception(ret['message'] + ': ' + url)
    return ret


def get_json_value(json_obj, key):
    """Gets the value of the given Json key.
    Key should be in the form <parent>[/<child>]* if not in the root of the tree.

    :type json_obj: dict
    :type key: str
    :rtype: dict | list | str | int | long | float | True | False | None
    """
    value = json_obj
    splitted = key.split('/')
    for subkey in splitted:
        value = value[subkey]
    return value


# DECK LIST METHODS

def get_deck_list(full_list=False, search=None, author=None, category=None, limit=0, offset=0):
    """Gets a list of deck info dicts.

    :type full_list: True | False
    :type search: str
    :type author: str
    :type category: str
    :type limit: int
    :type offset: int
    :rtype: list
    """
    deck_list_json = get_deck_list_json(search=search, author=author, category=category, limit=limit, offset=offset)
    count = get_json_value(deck_list_json, constants.PATH_DECK_LIST_COUNT)
    deck_list_data = get_json_value(deck_list_json, constants.PATH_DECK_LIST_DATA)

    if full_list:
        if not (0 < limit <= 50):
            limit = constants.DECK_LIST_REQ_MAX_RESULTS

        offset += limit

        while count >= offset and offset <= constants.DECK_LIST_MAX_COUNT:
            deck_list_json = get_deck_list_json(search=search, author=author, category=category, limit=limit, offset=offset)
            deck_list_data.append(get_json_value(deck_list_json, constants.PATH_DECK_LIST_DATA))
            offset += limit

    return deck_list_data


def get_deck_list_json(search=None, author=None, category=None, limit=None, offset=0):
    """Gets json with a list of decks that meet the given criteria.

    Keys:
        total: int
        results: dict
            count: int
            offset: int
            data: list of dict
                name: str
                code: str
                created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)
                updated_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)
                category: str
                author: dict
                    id: str
                    username: str
                call_count: int
                response_count: int
                rating: float
                sample_calls: list of dict
                    id: str
                    text: list of str
                    created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)
                sample_responses: list of dict
                    id: str
                    text: list of str
                    created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)

    :type search: str
    :type author: str
    :type category: str
    :type limit: int
    :type offset: int
    :rtype: dict
    """
    return get_remote_json(get_deck_list_url(search=search, author=author, category=category, limit=limit, offset=offset))


def get_deck_list_url(search=None, author=None, category=None, limit=0, offset=0):
    """Builds the deck list API URL based on the given criteria.

    :type search: str
    :type author: str
    :type category: str
    :type limit: int
    :type offset: int
    """
    if 0 < limit <= 50:
        params = [constants.DECK_LIST_LIMIT_PRM % limit]
    else:
        params = [constants.DECK_LIST_LIMIT_PRM % constants.DECK_LIST_REQ_MAX_RESULTS]

    if offset > 0: params.append(constants.DECK_LIST_OFFSET_PRM % offset)
    if search: params.append(constants.DECK_LIST_SEARCH_PRM % search)
    if author: params.append(constants.DECK_LIST_AUTHOR_PRM % author)
    if category: params.append(constants.DECK_LIST_CATEGORY_PRM % category)

    return constants.DECK_LIST_URL + '?' + '&'.join(params)


# DECK INFO METHODS

def get_deck_info_json(deck_id):
    """Gets json info about the given deck ID.

    Keys:
        name: str
        code: str
        description: str
        unlisted: True | False
        created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)
        updated_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)
        external_copyright: True | False
        copyright_holder_url: str | None
        category: str
        author: dict
            id: str
            username: str
        call_count: int
        response_count: int
        rating: float

    :type deck_id: str
    :rtype: dict
    """
    return get_remote_json(constants.DECK_INFO_URL % deck_id)


def get_deck_cards_json(deck_id):
    """Gets json card data

    Keys:
        calls: list of dict
            id: str
            text: list of str
            created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)
        responses: list of dict
            id: str
            text: list of str
            created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)

    :type deck_id: str
    :rtype: dict
    """
    return get_remote_json(constants.CARDS_URL % deck_id)


def get_deck_blacks_json(deck_id):
    """Gets json black card data.

    list of dict
        id: str
        text: list of str
        created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)

    :type deck_id: str
    :rtype: list
    """
    return get_json_value(get_remote_json(constants.CARDS_URL % deck_id), 'calls')


def get_deck_cards_json(deck_id):
    """Gets json white card data.

    list of dict
        id: str
        text: list of str
        created_at: str (timestamp CCYY-MM-DD + "T" + hh:mm:ss+00:00)

    :type deck_id: str
    :rtype: list
    """
    return get_json_value(get_remote_json(constants.CARDS_URL % deck_id), 'responses')