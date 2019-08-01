from setuptools import setup

from .instagram_api.version import version

setup(
    name='instagram_api',
    version=version,
    description=(
        'Unofficial instagram API, give you access to ALL instagram features'
        ' (like, follow, upload photo and video and etc)!'
    ),
    url='https://github.com/Yuego/instagram_api/',
    author='Artem Vlasov',
    author_email='root@proscript.ru',
    license='MIT',
    packages=['instagram_api'],
    zip_safe=False,
    install_requires=list(open('./requirements.txt', 'r').readlines()),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
