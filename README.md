# IraWatch

This is a python client library which sends traces to IraWatch collector.

### Install 

```bash
pip install irawatch
```

### Example

```py
import asyncio
import time
import uuid
import nats

# It is important to have a import statement like this. `from irawatch.trace import Tracer, Span` won't work due to design considerations.
from irawatch import trace


async def main():
    nc = await nats.connect()

    # Initialise tracer when application starts up
    trace.Tracer(service_name="App L", nats_conn=nc)

    # The trace ID must be 16 bytes. UUID4 is 16 bytes, so can be used.
    trace_id = uuid.uuid4().bytes

    # Every time you want to send a trace, you do the following
    span = trace.Span(name="Task P", trace_id=trace_id).start()
    time.sleep(2) # some task
    await span.stop() # when you invoke stop, it will send the trace to the collector.

    span = trace.Span("Task Q", trace_id).start()
    time.sleep(3)
    await span.stop(attributes={"X": "Y"}) # the attributes argument takes dict where key is string and value is any valid JSON value


asyncio.run(main())
```