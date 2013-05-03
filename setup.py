
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1.0'

setup(name='plone_interact',
      version=version,
      description="",
      long_description=read('README.md'),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      keywords='plone',
      author='Enfold Systems, Inc.',
      author_email='info@enfoldsystems.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
              'Products.PloneTestCase',
          ]
      ),
      install_requires=[
          'setuptools',
          "plone.portlets",
          "plone.app.portlets",
          "plone.app.form>=1.1",
          "plone.i18n",
          'zope.component',
          'zope.formlib',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
          'Zope2',
          'firebase_token_generator',
          'requests',
          'python-firebase==0.1.0',
      ],
      dependency_links=[
          # Needs github master at the moment, because pypi egg is borken with README.md not found.
          'http://github.com/reebalazs/firebase-token-generator-python/tarball/master#egg=firebase_token_generator-1.3',
          # It looks like this one has two spawns with the same name?
          # Make sure we use this one and not version 1.0 from pypi.
          'http://github.com/mikexstudios/python-firebase/tarball/master#egg=python-firebase-0.1.0',
      ],
      entry_points="""

      [z3c.autoinclude.plugin]
      target = plone

      [console_scripts]
      interact_put = plone_interact.scripts.interact_put:main
      interact_get = plone_interact.scripts.interact_get:main
      """,
      )
