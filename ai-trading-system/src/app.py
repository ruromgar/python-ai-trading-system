import asyncio

from application.clients.logger_client import LoggerClient
from application.clients.yahoo_client import YahooClient
from application.clients.alpaca_client import AlpacaClient
from application.clients.robinhood_client import RobinHoodClient
from application.clients.ai_client import AIClient
from application.repositories.yahoo_repository import YahooRepository
from application.repositories.ai_repository import AIRepository
from application.actions.trading_system import TradingSystem

from config import config


class Container:

    def __init__(self):
        self._logger = LoggerClient(config).get_logger()
        self._logger.info("AI trading system starting...")

        self._yahoo_client = YahooClient(self._logger, config)
        self._yahoo_repository = YahooRepository(self._logger, config, self._yahoo_client)
        self._ai_client = AIClient(self._logger, config)
        self._ai_repository = AIRepository(self._logger, config, self._ai_client)
        self._trading_system = TradingSystem(
            self._logger, config, self._yahoo_repository, self._ai_repository)

    async def start_monitoring(self):
        await self._trading_system.monitoring(config.POLLING_CONFIG['yahoo_interval'], exec_on_start=True)


if __name__ == '__main__':
    container = Container()
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(container.start_monitoring(), loop=loop)
    loop.run_forever()
