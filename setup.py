from setuptools import setup, find_packages

setup(
        name='pytimesheet',
        version='0.0.12',
        license='GPL',
        description='timetracking for hiwis at tu darmstadt',
        install_requires =['Jinja2'],
        packages=find_packages(),
        include_package_data=True,
        package_data = {'pytimesheet': ['template/*', 'config.ini']},
        entry_points={
            'console_scripts': [
                'pytimesheet=pytimesheet.cli:main',
            ],
        }
)
