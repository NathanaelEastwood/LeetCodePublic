class MyCalendarTwo:

    def __init__(self):
        self.start_dates = []
        self.end_dates = []

    def book(self, start: int, end: int) -> bool:
        is_tripled_booked = False
        booking_overlaps = 0
        for i in range(0, len(self.start_dates)):
            if self.start_dates[i] <= start < self.end_dates[i] or self.start_dates[i] < end <= self.end_dates[i]:
                booking_overlaps += 1

        if booking_overlaps >= 2:
            is_tripled_booked = True

        if not is_tripled_booked:
            self.start_dates.append(start)
            self.end_dates.append(end)

        return not is_tripled_booked

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)