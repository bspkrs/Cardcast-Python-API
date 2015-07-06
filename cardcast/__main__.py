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


from __future__ import print_function

from optparse import OptionParser
from cardcast import __version__, api, constants


def main():
    parser = OptionParser(version='%prog ' + __version__,
                          usage="%prog [options]")
    parser.add_option('-t', '--task', default=None, help='[REQUIRED] Valid tasks are [deckslist, deckinfo, cards, blacks, whites]')
    parser.add_option('-d', '--deck', default=None, help='The deck ID. REQUIRED for deckinfo, cards, blacks, and whites tasks, ignored otherwise.')
    parser.add_option('-a', '--author', default=None, help='A user name to search for. Used with the deckslist task, otherwise ignored.')
    parser.add_option('-c', '--category', default=None, help='A category to search for. Used with the deckslist task, otherwise ignored.')
    parser.add_option('-s', '--search', default=None, help='Keywords to search for. Used with the deckslist task, otherwise ignored.')
    parser.add_option('-n', '--num-results', default=constants.DECK_LIST_REQ_MAX_RESULTS, help='The number of results to return with the deckslist task. [default: %default]')
    parser.add_option('-o', '--offset', default=0, help='The number of decks to offset the result window returned by the deckslist task. [default: %default]')

    options, args = parser.parse_args()

    if not options.task:
        parser.print_help()
        exit(1)

    if not options.task in ['deckslist', 'deckinfo', 'cards', 'blacks', 'whites']:
        print('Invalid task specified: %s' % options.task)
        parser.print_help()
        exit(2)

    if options.task in ['deckinfo', 'cards', 'blacks', 'whites']:
        if not options.deck:
            print('Task %s requires a deck ID to be specified using the -d option.' % options.task)
            parser.print_help()
            exit(3)

        if options.task == 'deckinfo':
            print(api.get_deck_info_json(options.deck))
        elif options.task == 'cards':
            print(api.get_deck_cards_json(options.deck))
        elif options.task == 'blacks':
            print(api.get_deck_blacks_json(options.deck))
        elif options.task == 'whites':
            print(api.get_deck_whites_json(options.deck))
    else:
        print(api.get_deck_list_json(search=options.search, author=options.author, category=options.category, limit=options.num_results, offset=options.offset))



if __name__ == "__main__":
    main()
