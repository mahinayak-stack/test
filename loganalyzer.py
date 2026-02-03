from collections import defaultdict, Counter
from datetime import datetime

logs = [
    {"timestamp": "2026-02-02 10:15:23", "log_level": "ERROR", "message": "Database connection failed", "user_id": 101},
    {"timestamp": "2026-02-02 10:17:45", "log_level": "INFO", "message": "User login successful", "user_id": 102},
    {"timestamp": "2026-02-02 11:02:10", "log_level": "WARNING", "message": "Disk usage high", "user_id": 101},
    {"timestamp": "2026-02-02 11:15:55", "log_level": "ERROR", "message": "Timeout while calling API", "user_id": 103},
    {"timestamp": "2026-02-02 11:45:00", "log_level": "ERROR", "message": "Database connection failed", "user_id": 101},
    {"timestamp": "2026-02-02 12:05:30", "log_level": "INFO", "message": "File uploaded", "user_id": 104},
    {"timestamp": "2026-02-02 12:15:42", "log_level": "ERROR", "message": "Timeout while calling API", "user_id": 103},
]
error_logs = [log for log in logs if log["log_level"] == "ERROR"]
warning_logs = [log for log in logs if log["log_level"] == "WARNING"]
info_logs = [log for log in logs if log["log_level"] == "INFO"]

#number of logs of one particular type
log_level_count = Counter(log["log_level"] for log in logs)

user_activity = Counter(log["user_id"] for log in logs)
most_active_user = user_activity.most_common(1)[0]
errors_by_hour = defaultdict(int)

for log in error_logs:
    hour = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S").hour
    errors_by_hour[hour] += 1
    
error_messages = Counter(log["message"] for log in error_logs)
top_5_errors = error_messages.most_common(5)
peak_error_hour = max(errors_by_hour.items(), key=lambda x: x[1])
total_logs = len(logs)
total_errors = log_level_count["ERROR"]
error_rate = (total_errors / total_logs) * 100
print("LOG ANALYSIS REPORT")
print("-" * 30)
print(f"Total logs processed: {total_logs}")
print(f"Error rate: {error_rate:.2f}%")
print(f"Log level counts: {dict(log_level_count)}")
print(f"Most active user: User {most_active_user[0]} ({most_active_user[1]} actions)")
print(f"Peak error hour: {peak_error_hour[0]}:00 with {peak_error_hour[1]} errors")
print("\nTop 5 Error Messages:")
for msg, count in top_5_errors:
    print(f"- {msg} ({count} times)")