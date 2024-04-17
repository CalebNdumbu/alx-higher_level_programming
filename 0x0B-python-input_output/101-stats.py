import sys

valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

total_file_size = 0
status_code_counts = {code: 0 for code in valid_status_codes}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.strip().split()
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except (ValueError, IndexError):
            continue

        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_code_counts.keys()):
                count = status_code_counts[code]
                if count > 0:
                    print(code + ":", count)

except KeyboardInterrupt:
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(code + ":", count)
