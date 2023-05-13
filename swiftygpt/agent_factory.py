from swiftygpt.agent import SampleAgent
from swiftygpt.messaging.message_broker import MessageBroker
from swiftygpt.messaging.queue_channel import QueueChannel


def build_agent(name: str, channel: QueueChannel):
    """Build the agent."""
    print("Building agent...")
    message_broker = MessageBroker(channels=[channel])
    return SampleAgent(uid=name, name=name, message_broker=message_broker)
