Cardcast-Python-API
===================

A collection of Python scripts for interacting with the Cardcast API at cardcastgame.com

## Setup
1. Clone this repo.
2. From a terminal execute <code>python setup.py install</code> from the root of the cloned repo

## Usage
Type <code>python cardcast</code> for usage info.

<code>Options:
  --version             show program's version number and exit  
  -h, --help            show this help message and exit  
  -t TASK, --task=TASK  [REQUIRED] Valid tasks are [deckslist, deckinfo, cards, blacks, whites]  
  -d DECK, --deck=DECK  The deck ID. REQUIRED for deckinfo, cards, blacks, and whites tasks, ignored otherwise.  
  -a AUTHOR, --author=AUTHOR   
                        A user name to search for. Used with the deckslist task, otherwise ignored.  
  -c CATEGORY, --category=CATEGORY  
                        A category to search for. Used with the deckslist task, otherwise ignored.  
  -s SEARCH, --search=SEARCH  
                        Keywords to search for. Used with the deckslist task, otherwise ignored.  
  -n NUM_RESULTS, --num-results=NUM_RESULTS  
                        The number of results to return with the deckslist task. [default: 50]  
  -o OFFSET, --offset=OFFSET  
                        The number of decks to offset the result window returned by the deckslist task. [default: 0]<code/>  