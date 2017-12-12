try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The first and only triathlon coaching game, where you coach a triathlete.',
    'author': 'Marcel Cahenzli',
    'url': 'Currently not available.',
    'download_url': 'Currently not available.',
    'author_email': 'Currently not available.'
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TriCoaCH_Game'],
    'scripts': [],
    'name': 'TriCoaCH-Project'
}

setup(**config)
