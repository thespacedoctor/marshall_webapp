from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/marshall_webapp/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.rst') as f:
        return f.read()

install_requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'paste',
    'sqlalchemy',
    'fundamentals',
    'mod_wsgi'
]

# READ THE DOCS SERVERS
exists = os.path.exists("/home/docs/")
if exists:
    c_exclude_list = ['healpy', 'astropy',
                      'numpy', 'sherlock', 'wcsaxes', 'HMpTy', 'ligo-gracedb']
    for e in c_exclude_list:
        try:
            install_requires.remove(e)
        except:
            pass


setup(name='marshall_webapp',
      version=__version__,
      description='The web application for the transient marshall',
      long_description=readme(),
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      url='',
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      keywords=['web, pyramid, pylons'],
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='nose2.collector.collector',
      tests_require=['nose2', 'cov-core'],
      entry_points={
          'paste.app_factory': ['main=marshall_webapp:main', ],
      },
      zip_safe=False,
      )
