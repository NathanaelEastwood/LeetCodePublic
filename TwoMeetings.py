input = [{
        "callId": "2c269d25-deb9-42cf-927c-543112f7a76b",
        "startTimestamp": 10,
        "endTimestamp": 30
    },
    {
        "callId": "2c269d25-deb9-42cf-927c-543112f7a76c",
        "startTimestamp": 20,
        "endTimestamp": 30
    },
    {
        "callId": "2c269d25-deb9-42cf-927c-543112f7a76d",
        "startTimestamp": 20,
        "endTimestamp": 40
    }
]

def meetingRooms(intervals):
    time = []
    for i in intervals:
        time.append(([i["startTimestamp"], i["callId"]], 1))
        time.append(([i["endTimestamp"], i["callId"]], -1))

    # Change this if we need to adjust how overlapping calls are handled.
    time.sort(key = lambda x: (x[0][0], x[1]))

    res, count = 0, 0
    concurrent_ids = []
    result_ids = []

    for t in time:
        if t[1] == 1:
            count += 1
            concurrent_ids.append(t[0][1])
        else:
            count -= 1
            concurrent_ids.remove(t[0][1])

        if count > res:
            res = count
            result_ids = concurrent_ids.copy()

    return res, result_ids

print(meetingRooms(input))


