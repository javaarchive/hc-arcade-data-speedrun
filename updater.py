import arcade_airtable_requests
import csv
import time
from datetime import datetime

TABLE_WITH_COLS = "tblXCMI4Rp3KwMVHA"
COL = "fldBU1XI8cbCtMnyi"
PENDING_TABLE = "tblInG5Kg3SlVKNob"

def get_current_datetime_str():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# average csv pipeline I borrowed from stackoverflow
with open("data.csv", "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        "Time",
        "Formatted Time",
        "Hours Approved",
        "Hours Pending"
    ])
    while True:
        try:
            print("Fetching new data for airtable")
            airtable_data = arcade_airtable_requests.download_table()["data"]
            totals = {}
            #for query_slice in airtable_data["preloadPageQueryResults"]["querySlices"]:
            #    table_id = query_slice["tableId"]
            #    results[table_id] = len(query_slice["rowIds"])
            tables = airtable_data["preloadPageQueryResults"]["tableDataById"]
            for table_id in tables:
                table = tables[table_id]
                partial_rows = table["partialRowById"]
                # tblu has countries
                totals[table_id] = len(partial_rows)

            hours_sum = 0
            for row_id in tables[TABLE_WITH_COLS]["partialRowById"]:
                hours = tables[TABLE_WITH_COLS]["partialRowById"][row_id]["cellValuesByColumnId"][COL]
                hours_sum += hours
            print(totals, totals[PENDING_TABLE])
            print(hours_sum)

            writer.writerow({
                "Time": int(time.time()),
                "Formatted Time": get_current_datetime_str(),
                "Hours Approved": hours_sum,
                "Hours Pending": totals[PENDING_TABLE]
            })
            csvfile.flush()


        except Exception as ex:
            print("exception", ex)
            time.sleep(30)

        time.sleep(60)