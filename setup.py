from setuptools import setup

setup(name='wherethedjeck',
      version='0.1.2',
      description='Quickly find where the heck things are in Django framework',
      url='https://github.com/ramonsaraiva/wherethedjeck',
      author='Ramon Saraiva',
      author_email='ramonsaraiva@gmail.com',
      license='MIT',
      packages=['wherethedjeck'],
      scripts=['wherethedjeck/bin/wtd'],
      zip_safe=False)
