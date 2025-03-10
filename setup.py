import setuptools


setuptools.setup(

    name="selfforwarder",
    version="1",

    license="AGPL-3.0",

    author="NirZak",
    author_email="nirzashzakilim@gmail.com",

    install_requires=[
        "python-telegram-bot==13.14",
        "Pyyaml"
    ],

    packages=[
        "selfforwarder",
    ],

    entry_points={
        "console_scripts": [
            "selfforwarder = selfforwarder.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
