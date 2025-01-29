from datetime import datetime

# Get current date/time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open("version.md", "w") as f:
    f.write(current_time)