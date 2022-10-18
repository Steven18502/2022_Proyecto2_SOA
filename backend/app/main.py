from event_handler import consume
from api import run
import threading

# Create a thread and run the consumer function
consume_thread = threading.Thread(target=consume, args=())
consume_thread.start()

# Run api
run()