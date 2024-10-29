import os
from datetime import datetime, timedelta

def create_files(start_date, end_date):
    # Convert input dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y%m%d")
    end_date = datetime.strptime(end_date, "%Y%m%d")
    
    # Iterate over the date range
    current_date = start_date
    while current_date <= end_date:
        # Format the date and create filename
        filename = f"UV{current_date.strftime('%Y%m%d')}.TRANS"
        # Use touch command to create an empty file
        with open(filename, 'w') as f:
            pass
        print(f"Created: {filename}")
        # Move to the next day
        current_date += timedelta(days=1)

# Usage
create_files("20240501", "20240813")
