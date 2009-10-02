from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='nfg.webfonts',
      version=version,
      description="Plone integration for WebFonts.biz",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='webfonts',
      author='NFG Net Facilities Group BV',
      author_email='support@nfg.nl',
      url='http://webfonts.biz',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nfg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
