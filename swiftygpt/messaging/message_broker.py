"""This module contains the message broker class."""
from swiftygpt.schema import BaseMessage, BaseMessageBroker, BaseMessageChannel


class MessageBroker(BaseMessageBroker):
    """A message broker that holds all the channels an agent can communicate on."""

    def __init__(self, channels: list[BaseMessageChannel]) -> None:
        """Initializes a message broker."""
        self.channels = channels

    def list_channels(self) -> None:
        """Lists all the channels."""
        return self.channels

    def get_channel(self, channel_uid: str) -> BaseMessageChannel:
        """Gets a channel."""
        return next(channel for channel in self.channels if channel.id == channel_uid)

    def get_channel_by_name(self, channel_name: str) -> BaseMessageChannel:
        """Gets a channel by name."""
        return next(
            channel for channel in self.channels if channel.name == channel_name
        )

    def add_channel(self, channel: BaseMessageChannel) -> None:
        """Adds a channel."""
        self.channels.append(channel)

    async def get_from_channel(self, channel_uid: str) -> BaseMessage:
        """Gets a message from a channel."""
        return self.get_channel(channel_uid).get()

    async def send_to_channel(self, channel_uid: str, message: BaseMessage) -> None:
        """Sends a message to a channel."""
        return self.get_channel(channel_uid).send(message)
