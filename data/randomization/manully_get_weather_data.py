import csv
import requests
import datetime
import schedule
import time

# Define the URL and parameters for fetching the data
url = "http://www-k12.atmos.washington.edu/k12/grayskies/plot_nw_wx.cgi"
params = {
    "Measurement": ["Temperature", "Relhum", "Speed", "Direction", "Pressure", "Solar", "SumRain", "Rain"],
    "station": "UWA",
    "interval": "0",
    "timezone": "0",
    "rightlab": "y",
    "connect": "dataonly",
    "groupby": "overlay",
    "begmonth": "6",
    "begday": "1",
    "begyear": "2022",
    "beghour": "0",
    "endmonth": str(datetime.datetime.now().month),
    "endday": str(datetime.datetime.now().day),
    "endyear": str(datetime.datetime.now().year),
    "endhour": "23"
}

csv_file = "2022-2023-uwa.csv"

def fetch_data():
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.text

        # Write the data to a CSV file
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            for row in data.splitlines():
                split_data = row.split(",")
                writer.writerow(split_data)

        print(f"Data fetched and saved successfully. File saved at: {csv_file}")

def job():
    print("Checking for new data...")
    fetch_data()
    print("Data fetch and save completed.")

# Run the job immediately when you press "run"
job()

# Schedule the job to run every hour
schedule.every().hour.do(job)

# Run the scheduler in an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)