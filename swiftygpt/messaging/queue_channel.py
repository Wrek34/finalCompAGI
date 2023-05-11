"""Basic in memory implementation using Asyncio queues."""
import asyncio.queues

from swiftygpt.schema import BaseMessage, BaseMessageChannel


class QueueChannel(BaseMessageChannel):
    """A queue channel that messages can be sent and received on."""

    def __init__(self, name: str, host: str, port: int) -> None:
        """Initializes a queue channel."""
        self.name = name
        self.id = name
        self.host = host
        self.port = port
        self.queue = asyncio.queues.Queue()

    async def get(self) -> BaseMessage:
        """Gets a message from the channel."""
        msg = await self.queue.get()
        self.received_message_count += 1
        self.received_bytes_count += len(msg)
        return msg

    async def send(self, message: BaseMessage) -> None:
        """Sends a message to the channel."""
        self.sent_message_count += 1
        self.send_bytes_count += len(message)
        await self.queue.put(message)
