from distutils.core import setup

import cardcast

setup(name='Cardcast-Python-API',
      version=cardcast.__version__,
      description='Python Wrapper for the Cardcastgame.com API',
      author='bspkrs',
      author_email='bspkrs@gmail.com',
      url='https://github.com/bspkrs/Cardcast-Python-API',
      packages=['cardcast'],
      )