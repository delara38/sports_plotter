from setuptools import setup

setup(name='sports_plotter',
      version='0.2',
      description='package making it easier to plot on soccer pitches and hockey rinks',
      download_url = 'https://github.com/delara38/sports_plotter/archive/0.1.tar.gz',
      url='https://github.com/delara38/sports_plotter',
      author='Nathan de Lara',
      author_email='natan.de.lara@gmail.com',
      license='MIT',
      packages=['sports_plotter'],
      install_requires = ['matplotlib','numpy','pandas'],
      zip_safe=False)
