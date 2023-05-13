import pydantic

############################
##### Messaging Schema #####
############################


class BaseMessage(pydantic.BaseModel):
    """Base class for a message that can be sent and received on a channel."""

    from_uid: str
    to_uid: str
    timestamp: int


class BaseMessageChannel(pydantic.BaseModel):
    """Base class for a channel that messages can be sent and received on"""

    id: str
    name: str
    host: str
    port: int

    # Channel statistics
    sent_message_count: int = 0
    sent_bytes_count: int = 0
    received_message_count: int = 0
    received_bytes_count: int = 0

    def __str__(self) -> str:
        f"Channel {self.name}:({self.id}) on {self.host}:{self.port}"
        return f"Channel {self.name}:({self.id}) on {self.host}:{self.port}"

    async def get(self) -> None:
        """Gets a message from the channel."""
        raise NotImplementedError

    async def send(self) -> None:
        """Sends a message to the channel."""
        raise NotImplementedError


class BaseMessageBroker(pydantic.BaseModel):
    """Base class for message brokers that holds all the channels an agent can communicate on."""

    channels: list[BaseMessageChannel]

    def list_channels(self) -> None:
        """Lists all the channels."""
        raise NotImplementedError

    def get_channel(self, channel_uid: str) -> BaseMessageChannel:
        """Gets a channel."""
        raise NotImplementedError

    def get_channel_by_name(self, channel_name: str) -> BaseMessageChannel:
        """Gets a channel by name."""
        raise NotImplementedError

    def add_channel(self, channel: BaseMessageChannel) -> None:
        """Adds a channel."""
        raise NotImplementedError

    async def get_from_channel(self, channel_uid: str) -> BaseMessage:
        """Gets a message from a channel."""
        raise NotImplementedError

    async def send_to_channel(self, channel_uid: str, message: BaseMessage) -> None:
        """Sends a message to a channel."""
        raise NotImplementedError


############################
####### Agent Schema #######
############################


class BaseAgent(pydantic.BaseModel):
    """A Base Agent Class"""

    uid: str
    message_broker: BaseMessageBroker

    async def run(self) -> None:
        """Runs the agent"""
        raise NotImplementedError

    async def stop(self) -> None:
        """Stops the agent"""
        raise NotImplementedError
