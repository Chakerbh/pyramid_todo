from setuptools import setup, find_packages

setup(name='todo',
      version='0.0',
      description='todo application',
      packages=find_packages(),
      entry_points="""\
      [paste.app_factory]
      main = todo:main
      """,
      )
