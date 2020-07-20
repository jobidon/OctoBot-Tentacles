#  Drakkar-Software OctoBot-Tentacles
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
from octobot_trading.exchanges.types.spot_exchange import SpotExchange


class Kraken(SpotExchange):
    DESCRIPTION = ""

    RECENT_TRADE_FIXED_LIMIT = 1000

    @classmethod
    def get_name(cls):
        return 'kraken'

    async def get_recent_trades(self, symbol, limit=RECENT_TRADE_FIXED_LIMIT, params=None):
        if limit is not None and limit != self.RECENT_TRADE_FIXED_LIMIT:
            self.logger.debug(f"Trying to get_recent_trades with limit != {self.RECENT_TRADE_FIXED_LIMIT} : ({limit})")
            limit = self.RECENT_TRADE_FIXED_LIMIT
        return await SpotExchange.get_recent_trades(self, symbol=symbol, limit=limit, params=params)