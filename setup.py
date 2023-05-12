from distutils.core import setup
import py2exe

options = {
    'py2exe': {
        'includes': [

            'os',
            'json'
        ],
        'packages': ['selenium',],
        'bundle_files': 1,
        'compressed': True,
    }
}

setup(
    options=options,
    console=['main.py'],
    zipfile=None,
)
