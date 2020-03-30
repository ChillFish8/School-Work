import asyncio
import logging


logging.basicConfig(level=logging.INFO)


# Server side -> move to different file to test

async def server_trigger(message, addr):
    """ Random coro server sends messages to """
    print(message)


class Server:
    """ Server Side """
    def __init__(self, message_event: asyncio.coroutine, loop=None, address='127.0.0.1', port=8888):
        self._loop = loop if loop is not None else asyncio.get_event_loop()
        self.message_event = message_event
        self.address = address
        self.port = port
        self.server_coro = None
        self.server = None

    async def receiver(self, reader, writer):
        data = await reader.read()     # Listens to all data sent
        message = data.decode()
        sender_details = writer.get_extra_info('peername')
        logging.log(logging.INFO, f"Got response from {sender_details}")
        await self.message_event(message, sender_details)

    async def run_server(self):
        self.server = self._loop.run_until_complete(self.server_coro)
        logging.log(logging.INFO, f'Serving on {self.server.sockets[0].getsockname()}')
        try:
            self._loop.run_forever()
        except KeyboardInterrupt:
            pass    # context manager handles this

    async def __aenter__(self):
        self.server_coro = asyncio.start_server(self.receiver, self.address, self.port, loop=self._loop)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.server is not None:
            self.server.close()
            self._loop.run_until_complete(self.server.wat_closed())
        if self._loop.is_running():
            self._loop.close()
        self._loop.close()


class Client:
    """ CLIENT SIDE """
    def __init__(self, loop=None):
        self._loop = loop if loop is not None else asyncio.get_event_loop()
        self.reader = None
        self.writer = None

    async def connect(self, address='127.0.0.1', port=8888):
        self.reader, self.writer = await asyncio.open_connection(address, port, loop=self._loop)
        logging.log(logging.INFO, f"TCP client connection opened on address {address}:{port}")

    async def send(self, message: str):
        self.writer.write(message.encode())
        logging.log(logging.INFO, f"Sent message {message}")
        return await self.read()

    async def read(self):
        data = await self.reader.read()
        logging.log(logging.INFO, f"Received response!")
        return data.decode()

    async def __aenter__(self):
        await self.connect()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.writer is not None:
            await self.writer.close()
            await self.reader.close()
        if self._loop.is_running():
            await self._loop.shutdown_asyncgens()
            self._loop.stop()
        else:
            self._loop.close()
