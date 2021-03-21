import time


def _tail_print(e):
    print("%s %s %s" % (e.resource_status, e.resource_type, e.event_id))


def get_events(conn, stackname):
    """Get the events in batches and return in chronological order"""
    next = None
    event_list = []
    while 1:
        events = conn.describe_stack_events(stackname, next)
        event_list.append(events)
        if events.next_token is None:
            break
        next = events.next_token
        time.sleep(1)
    return reversed(sum(event_list, []))


def tail(conn, stack_name, log_func=_tail_print, sleep_time=5,
         include_initial=True):
    """Show and then tail the event log"""
    # First dump the full list of events in chronological order and keep
    # track of the events we've seen already
    seen = set()
    initial_events = get_events(conn, stack_name)
    for e in initial_events:
        if include_initial:
            log_func(e)
        seen.add(e.event_id)

    # Now keep looping through and dump the new events
    while 1:
        events = get_events(conn, stack_name)
        for e in events:
            if e.event_id not in seen:
                log_func(e)
                seen.add(e.event_id)
        time.sleep(sleep_time)
