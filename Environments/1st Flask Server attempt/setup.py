from setuptools import setup, find_packages

requires = [
	'flask',
	'flask-sqlachemy',
	'psycopg2',
]

setup(
	name='flask_pool',
	version='0.0',
	description='My first ever application built with Flask',
	author='Nana Yaw Amfo-Brobbey',
	author_email='nana.amfobrobbey@gmail.com',
	keywords='web flask',
	packages=find_packages(),
	include_package_data=True,
	install_requires=requires
)
