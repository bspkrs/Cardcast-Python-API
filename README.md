Cardcast-Python-API
===================

A collection of Python scripts for interacting with the Cardcast API at cardcastgame.com

## Setup
1. Clone this repo.
2. From a terminal execute <code>python setup.py install</code> from the root of the cloned repo

## Usage
Type '''python cardcast''' for usage info.

Options:<br/>
  --version             show program's version number and exit<br/>
  -h, --help            show this help message and exit<br/>
  -t TASK, --task=TASK  [REQUIRED] Valid tasks are [deckslist, deckinfo, cards, blacks, whites]<br/>
  -d DECK, --deck=DECK  The deck ID. REQUIRED for deckinfo, cards, blacks, and whites tasks, ignored otherwise.<br/>
  -a AUTHOR, --author=AUTHOR <br/>
                        A user name to search for. Used with the deckslist task, otherwise ignored.<br/>
  -c CATEGORY, --category=CATEGORY<br/>
                        A category to search for. Used with the deckslist task, otherwise ignored.<br/>
  -s SEARCH, --search=SEARCH<br/>
                        Keywords to search for. Used with the deckslist task, otherwise ignored.<br/>
  -n NUM_RESULTS, --num-results=NUM_RESULTS<br/>
                        The number of results to return with the deckslist task. [default: 50]<br/>
  -o OFFSET, --offset=OFFSET<br/>
                        The number of decks to offset the result window returned by the deckslist task. [default: 0]<br/>