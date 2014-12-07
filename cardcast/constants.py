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


# Default folder to save data
DEFAULT_LOCAL_DIR = './deck_data'

# JSON paths
PATH_DECK_LIST_DATA = 'results/data'
PATH_DECK_LIST_COUNT = 'results/count'

# ID of invalid resource requests
RESOURCE_NOT_FOUND = 'not_found'

# The API domain name.
HOSTNAME = 'api.cardcastgame.com'

# The base URL to get a list of decks.
DECK_LIST_URL = 'https://%s/v1/decks' % HOSTNAME

# Deck List URL parameters
DECK_LIST_OFFSET_PRM = 'offset=%d'
DECK_LIST_LIMIT_PRM = 'limit=%d'
DECK_LIST_SEARCH_PRM = 'search=%s'
DECK_LIST_AUTHOR_PRM = 'author=%s'
DECK_LIST_CATEGORY_PRM = 'category=%s'

# Max number of deck records returned per request
# Default: 50, valid range 1-50
DECK_LIST_REQ_MAX_RESULTS = 50
""":type: int"""

# Max number of decks allowed to be requested when attempting to get all results
# Default: 200
DECK_LIST_MAX_COUNT = 200
""":type: int"""

# The URL to get info about a deck. Replacement string is the deck ID.
DECK_INFO_URL = DECK_LIST_URL + '/%s'

# The URL to get card data for a deck. Replacement string is the deck ID.
CARDS_URL = DECK_INFO_URL + '/cards'
