From PyPI with pip:

::

    $pip install googlefinance

From development repo (requires git)

::

    $git clone https://github.com/hongtaocai/googlefinance.git
    $cd googlefinance
    $python setup.py install

    from googlefinance import getQuotes
    >>> import json
    >>> print json.dumps(getQuotes('AAPL'), indent=2)
