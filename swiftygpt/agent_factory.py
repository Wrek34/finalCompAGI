import os

from swiftygpt.agent import SampleAgent
from swiftygpt.LLM.openai_povider import OpenAIProvider
from swiftygpt.messaging.message_broker import MessageBroker
from swiftygpt.messaging.queue_channel import QueueChannel


def build_agent(name: str, channel: QueueChannel):
    """Build the agent."""
    print("Building agent...")
    # get api key from env
    api_key = os.getenv("OPENAI_API_KEY")
    llm_provider = OpenAIProvider(api_key=api_key, debug_mode=True)
    message_broker = MessageBroker(channels=[channel])
    return SampleAgent(
        uid=name, name=name, llm_provider=llm_provider, message_broker=message_broker
    )
