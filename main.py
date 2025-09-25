from datetime import datetime, timedelta

def generate_sbt_pull_commands():
    start_date = datetime(2025, 7, 20, 0, 0, 0)
    end_date = datetime(2025, 9, 9, 23, 59, 59)

    commands = []
    current_date = start_date

    while current_date <= end_date:
        hour_end = current_date + timedelta(hours=1) - timedelta(seconds=1)

        if hour_end > end_date:
            hour_end = end_date

        start_str = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        end_str = hour_end.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Inbound command
        inbound_cmd = f'python "D:\\batch_files\\py_files\\SBT API Message Pull.py" --env-file D:\\Massena\\Analytics\\Internal\\Internal11.txt --fetch-all --start-timestamp {start_str} --end-timestamp {end_str} --direction inbound --page-size 1000 --use-db-groups'
        commands.append(inbound_cmd)

        # Outbound command
        outbound_cmd = f'python "D:\\batch_files\\py_files\\SBT API Message Pull.py" --env-file D:\\Massena\\Analytics\\Internal\\Internal11.txt --fetch-all --start-timestamp {start_str} --end-timestamp {end_str} --direction outbound --page-size 1000 --use-db-groups'
        commands.append(outbound_cmd)

        # Move to next hour
        current_date = current_date + timedelta(hours=1)

    # Write to .bat file
    with open("sbt_hourly_pull.bat", "w") as f:
        for cmd in commands:
            f.write(cmd + "\n")

    print(f"Generated {len(commands)} commands in sbt_hourly_pull.bat")
    print(f"Total hours covered: {len(commands) // 2}")
    print(f"Date range: {start_date.strftime('%Y-%m-%d %H:%M:%S')} to {end_date.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    generate_sbt_pull_commands()