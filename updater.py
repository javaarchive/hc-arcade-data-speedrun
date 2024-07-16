import arcade_airtable_requests
import csv
import time

with open("data.csv", "w"):
    writer = csv.DictWriter(csvfile, fieldnames={
        "Time",
        "Hours Approved",
        "Hours Pending"
    })
    writer.writerow({'This':'is', 'aNew':'Row'})
    while True:
        try:
            airtable_data = arcade_airtable_requests.download_table()
            results = {}
            for query_slice in airtable_data["preloadPageQueryResults"]["querySlices"]:
                table_id = query_slice["tableId"]
                results[table_id] = len(query_slice["rowIds"])

        except Exception as ex:
            print(ex)
            time.sleep(30)

        time.sleep(60)