lykkex-cli
=========

*Lykke exchange command line tool.*


Purpose
-------

Interested in [Lykke](https://www.lykke.com/) and loving the command line? This is your project. Interact seamlessly with the [Lykkex API](https://hft-service-dev.lykkex.net/swagger/ui/index.html#/) via lykkex-cli. Check your balance and send trading orders in one line or automate your trading procedures.

Usage
-----

After installation, just type
```
lykkex
```
and discover how to trade on the Lykkex API.

Install
-------

If you've cloned this project, and want to install the library (*and all
development dependencies*), the command you'll want to run is::

    $ pip install -e .[test]

If you'd like to run all tests for this project (*assuming you've written
some*), you would run the following command::

    $ python setup.py test

This will trigger `py.test <http://pytest.org/latest/>`_.

Acknowledgements
----------------

This project is based on the [lykkex Python API wrapper](https://github.com/pfeffer90/lykkex). It is an offspring of the [Lykke Tradebot Repo](https://github.com/pfeffer90/pytr8). Thanks to the command line [skeleton repository](https://github.com/rdegges/skele-cli), which is also the backbone of this cli.
