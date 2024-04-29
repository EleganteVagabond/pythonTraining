""" This is a replica of the test I took with Headway on 10.24.2023"""

from datetime import datetime, timedelta
import sys
import unittest

""" Appointment format `yyyy-mm-dd hh:mm yyyy-mm-dd hh:mm`"""

DATE_FORMAT = "%Y-%m-%d %H:%M"
SCHEDULE_START = datetime.strptime("2024-01-01 09:00", DATE_FORMAT)


def parse_date(datetime_string):
    return datetime.strptime(datetime_string, DATE_FORMAT)


SCHEDULED_APPOINTMENTS_DATA = [
    ("2024-01-01 11:00", "2024-01-01 11:30"),
    ("2024-01-01 12:00", "2024-01-01 12:45"),
    ("2024-01-01 01:00", "2024-01-01 1:50"),
    ("2024-01-01 02:00", "2024-01-01 02:45"),
    ("2024-01-01 03:30", "2024-01-01 4:15"),
]


def parse_scheduled_appointments(schedule_array):
    parsed_appointments = []
    for appointments in schedule_array:
        start = parse_date(appointments[0])
        end = parse_date(appointments[1])
        parsed_appointments.append((start, end))
    return parsed_appointments


def calculate_time_difference_in_minutes(start_time, end_time):
    return (end_time - start_time).seconds // 60


def check_window(
    appointment_length, appointment_window, appointment_start_date, target_appointment
):
    if appointment_window >= appointment_length:
        projected_end_of_appt = appointment_start_date + timedelta(
            minutes=appointment_length
        )
        # if before the end of the day
        if projected_end_of_appt <= appointment_start_date.replace(hour=17, minute=0):
            if target_appointment == None or target_appointment[1] > appointment_window:
                return (appointment_start_date, appointment_window)

    return target_appointment


def evaluate_potential_appointment(
    start_datetime, end_datetime, appointment_length, target_appointment
):
    appointment_window = calculate_time_difference_in_minutes(
        start_datetime, end_datetime
    )
    target_appointment = check_window(
        appointment_length, appointment_window, start_datetime, target_appointment
    )
    return target_appointment


def schedule_appointment(scheduled_appointments, appointment_length):
    if appointment_length <= 0:
        raise ValueError

    if len(scheduled_appointments) == 0:
        return SCHEDULE_START

    target_appointment = None
    # check start of day for first appt
    target_appointment = evaluate_potential_appointment(
        scheduled_appointments[0][0].replace(hour=9, minute=0),
        scheduled_appointments[0][0],
        appointment_length,
        target_appointment,
    )
    if target_appointment != None and target_appointment[1] == appointment_length:
        return target_appointment[0]

    for appt_ix in range(len(scheduled_appointments) - 1):
        target_appointment = evaluate_potential_appointment(
            scheduled_appointments[appt_ix][1],
            scheduled_appointments[appt_ix + 1][0],
            appointment_length,
            target_appointment,
        )
        if target_appointment != None and target_appointment[1] == appointment_length:
            return target_appointment[0]

    # check end of day
    target_appointment = evaluate_potential_appointment(
        scheduled_appointments[-1][1],
        scheduled_appointments[-1][1].replace(hour=17, minute=0),
        appointment_length,
        target_appointment,
    )

    if target_appointment != None:
        return target_appointment[0]
    else:
        return scheduled_appointments[-1][1].replace(
            hour=9, minute=0, day=scheduled_appointments[-1][1].day + 1
        )


class TestScheduleAppointment(unittest.TestCase):
    def test_invalid_appointment_length(self):
        self.assertRaises(ValueError, schedule_appointment, [], 0)

        self.assertRaises(ValueError, schedule_appointment, [], -5)

    def test_empty_appointments(self):
        result = schedule_appointment([], 10)
        self.assertEqual(result, SCHEDULE_START)

        result = schedule_appointment([], 30)
        self.assertEqual(result, SCHEDULE_START)

    def test_perfect_match_appointment(self):
        test_data = [
            ("2024-01-01 11:00", "2024-01-01 11:30"),
            ("2024-01-01 12:00", "2024-01-01 12:45"),
            ("2024-01-01 13:00", "2024-01-01 13:50"),
            ("2024-01-01 14:00", "2024-01-01 14:45"),
            ("2024-01-01 15:30", "2024-01-01 16:15"),
        ]
        test_appointments = parse_scheduled_appointments(test_data)

        result = schedule_appointment(test_appointments, 45)
        self.assertEqual(result, parse_date("2024-01-01 14:45"))

        result = schedule_appointment(test_appointments, 30)
        self.assertEqual(result, parse_date("2024-01-01 11:30"))

    def test_minimum_best_appointment(self):
        test_data = [
            ("2024-01-01 11:00", "2024-01-01 11:30"),
            ("2024-01-01 12:00", "2024-01-01 12:45"),
            ("2024-01-01 13:00", "2024-01-01 13:50"),
            ("2024-01-01 14:00", "2024-01-01 14:45"),
            ("2024-01-01 15:30", "2024-01-01 16:00"),
        ]
        test_appointments = parse_scheduled_appointments(test_data)

        result = schedule_appointment(test_appointments, 20)
        self.assertEqual(result, parse_date("2024-01-01 11:30"))

        result = schedule_appointment(test_appointments, 10)
        self.assertEqual(result, parse_date("2024-01-01 13:50"))

    def test_end_of_day_appointment(self):
        test_data = [
            ("2024-01-01 15:30", "2024-01-01 16:00"),
        ]
        test_appointments = parse_scheduled_appointments(test_data)

        result = schedule_appointment(test_appointments, 60)
        self.assertEqual(result, parse_date("2024-01-01 16:00"))

    def test_end_of_day_appointment_with_rollover(self):
        test_data = [
            ("2024-01-01 09:00", "2024-01-01 10:30"),
            ("2024-01-01 11:00", "2024-01-01 11:30"),
            ("2024-01-01 12:00", "2024-01-01 12:45"),
            ("2024-01-01 13:00", "2024-01-01 13:50"),
            ("2024-01-01 14:00", "2024-01-01 14:45"),
            ("2024-01-01 15:30", "2024-01-01 16:00"),
        ]
        test_appointments = parse_scheduled_appointments(test_data)

        result = schedule_appointment(test_appointments, 75)
        self.assertEqual(result, parse_date("2024-01-02 09:00"))

    def test_start_of_day_appointment(self):
        test_data = [
            ("2024-01-01 11:00", "2024-01-01 11:30"),
            ("2024-01-01 12:00", "2024-01-01 12:45"),
            ("2024-01-01 13:00", "2024-01-01 13:50"),
            ("2024-01-01 14:00", "2024-01-01 14:45"),
            ("2024-01-01 15:30", "2024-01-01 16:15"),
        ]
        test_appointments = parse_scheduled_appointments(test_data)

        result = schedule_appointment(test_appointments, 60)
        self.assertEqual(result, parse_date("2024-01-01 09:00"))


def main():
    scheduled_appointments = (
        []
    )  # parse_scheduled_appointments(SCHEDULED_APPOINTMENTS_DATA)

    args = sys.argv[1:]
    new_appointment_length = args[0]

    new_appointment_date = schedule_appointment(
        scheduled_appointments, new_appointment_length
    )
    print(f"New appt: {new_appointment_date}")


if __name__ == "__main__":
    unittest.main()
