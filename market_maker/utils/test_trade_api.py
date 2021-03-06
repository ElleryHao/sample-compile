# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [View Changelog](/app/apiChangelog)    #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ##### Swagger Specification  [⇩ Download Swagger JSON](swagger.json)    ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

from rest import ApiException
from trade_api import TradeApi
import talib as ta
import numpy as np

class TestTradeApi(unittest.TestCase):
    """ TradeApi unit test stubs """

    def setUp(self):
        self.api = TradeApi()

    def tearDown(self):
        pass

    def test_trade_get(self):
        """
        Test case for trade_get

        Get Trades.
        """
        pass

    def test_trade_get_bucketed(self):
        """
        Test case for trade_get_bucketed

        Get previous trades in time buckets.
        """
        trades = (self.api.trade_get_bucketed(bin_size="1m",symbol="XBT",count=500,start_time="2017-11-03T00:14:11.891Z"))
        num=[]
        for trade in trades :
            print trade.close
            num.append(trade.close)
        print ta.MA(np.array(num),30)
        print ta.MA(np.array(num),60)

if __name__ == '__main__':
    unittest.main()
