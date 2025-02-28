# IraWatch

This is a client library which sends traces to IraWatch collector.

```py
nc = await nats.connect()

# Initialise tracer when application starts up
tracer = Tracer(service_name="App A", nc)

# Every time you want to send a trace, you do the following
span = tracer.span(name="Task A", trace_id=uuid.uuid4().bytes).start()
time.sleep(2) # some task
await span.stop() # when you say stop, it will send the trace to the collector.
```