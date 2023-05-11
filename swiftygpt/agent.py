import asyncio
import random

from swiftygpt.messaging.messages import (
    CommandMessage,
    InfoMessage,
    QueryMessage,
    ResponseMessage,
    StatusMessage,
)
from swiftygpt.schema import BaseAgent, BaseMessage, BaseMessageBroker


class SampleAgent(BaseAgent):
    """An async agent that can send a receive messages using a BaseMessage and process all subtypes of BaseMessage"""

    uid: str
    name: str
    message_broker: BaseMessageBroker

    def __init__(self, name: str, uid: str, message_broker: BaseMessageBroker):
        self.name = name
        self.uid = uid
        self.message_broker = message_broker

    def testing_random_action(self) -> None:
        """A random action for testing purposes"""
        roll = random.randint(1, 3)
        if roll == 1:
            self.message_broker.send_to_channel(
                "channel1", QueryMessage(query="What is the meaning of life?")
            )
        elif roll == 2:
            self.message_broker.send_to_channel(
                "channel1", CommandMessage(command="Do something!")
            )

    async def run(self) -> None:
        """Runs the agent"""
        while True:
            for channel in self.message_broker.channels:
                message = await channel.get()
                await self.process_message(message)
            # Perform a random action
            self.testing_random_action()
            # sleep 1 second
            await asyncio.sleep(1)

    async def process_message(self, message: BaseMessage) -> None:
        """Process an incoming message"""
        if isinstance(message, QueryMessage):
            await self.process_query(message)
        elif isinstance(message, CommandMessage):
            await self.process_command(message)
        elif isinstance(message, ResponseMessage):
            await self.process_response(message)
        elif isinstance(message, StatusMessage):
            await self.process_status(message)
        elif isinstance(message, InfoMessage):
            await self.process_info(message)
        else:
            print(f"Unknown message type: {type(message)}")

    async def process_query(self, message: QueryMessage) -> None:
        """Process a QueryMessage"""
        print(f"Agent: {self.uid} received query: {message.query}")

    async def process_command(self, message: CommandMessage) -> None:
        """Process a CommandMessage"""
        print(f"Agent: {self.uid} received command: {message.command}")

    async def process_response(self, message: ResponseMessage) -> None:
        """Process a ResponseMessage"""
        print(f"Agent: {self.uid} received response: {message.response}")

    async def process_status(self, message: StatusMessage) -> None:
        """Process a StatusMessage"""
        print(f"Agent: {self.uid} received status: {message.status}")

    async def process_info(self, message: InfoMessage) -> None:
        """Process an InfoMessage"""
        print(f"Agent: {self.uid} received info: {message.info}")
