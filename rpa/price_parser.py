import asyncio
from datetime import timedelta

from tinkoff.invest import AsyncClient, CandleInterval, Client
from tinkoff.invest.utils import now

from config import tinkoff_api_key

TOKEN = tinkoff_api_key

bounds = ['BBG00QDTJQD2', 'BBG00GKHR834']
shares = ['TCSS0A103VG1', 'LUZHNIKICOLL']
shares_pid = ['5c9c4a16-ec25-4eab-93af-e2827d22c146', 'cc54fe32-a3cd-4ec9-b21b-6038b6f6a522']
bounds_pid = ['0cd212ad-7e4e-45ba-9bf5-c7a415ff3e32', '5e8fa2d1-5b3b-41fc-a0ec-026f14a33a46']


# async def find_instrument():
#     instruments_list = []
#     async with AsyncClient(TOKEN) as client:
#         instruments = await client.instruments.find_instrument(query="тинькофф")
#         for instrument in instruments.instruments:
#             instruments_list.append(instrument)
#
#             if instrument.instrument_type == 'bond':
#                 print(instrument)


def parse_price():
    with Client(TOKEN) as client:
        for share in shares_pid:
            share = client.instruments.share_by(id_type=3, id=share)
            candle = client.market_data.get_candles(figi=share.instrument.figi, from_=now() - timedelta(hours=2),
                                                          to=now(), interval=CandleInterval.CANDLE_INTERVAL_HOUR)
            if not candle.candles:
                print('No candles')
                continue
            unit_open = candle.candles[0].open.units
            nano_open = candle.candles[0].open.nano
            unit_close = candle.candles[0].close.units
            nano_close = candle.candles[0].close.nano
            units_middle = (unit_open + unit_close) / 2
            nanos_middle = (nano_open + nano_close) / 2
            print(share.instrument.sector, units_middle, nanos_middle, share.instrument.name, share.instrument.currency)

        for bound in bounds_pid:
            bound = client.instruments.bond_by(id_type=3, id=bound)
            print(bound.instrument.nominal.units, bound.instrument.name, bound.instrument.currency)

parse_price()