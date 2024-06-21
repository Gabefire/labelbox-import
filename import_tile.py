import labelbox as lb
import os

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjazY3M25vd2E1ZWd3MDcwMGowYXFod3RxIiwib3JnYW5pemF0aW9uSWQiOiJjazY3M25vdTV4bTUxMDg0MnI2YWJsMWNjIiwiYXBpS2V5SWQiOiJjbHhvcnl2YzMwMGkwMDd6OTAwcm03cWRoIiwic2VjcmV0IjoiZmFjN2YyYWQyMTI3Zjk5ZDJkZmNjZDlmNzY5NzIwMDIiLCJpYXQiOjE3MTg5Nzk0MjcsImV4cCI6MjM1MDEzMTQyN30.xxfirYaQAg9JBM5Rj4bkEav9Uh47CAoAqT5WmxM-1iw"

data_rows = []

for file_name in os.listdir("./files_geospatial"):
    with open(f"./files_geospatial/{file_name}", "r") as file:
        for line in file.readlines():
            if not line:
                continue
            file_path = line[5:].rstrip()
            full_file = "https://storage.googleapis.com/" + file_path
            data_rows.append({
                "row_data": {"tileLayerUrl": full_file},
                "global_key": file_path,
            })

    client = lb.Client(API_KEY)

    dataset = client.create_dataset(name=file_name.replace("_", " ").rstrip(".txt"), iam_integration=None)

    task = dataset.create_data_rows(data_rows)
    task.wait_till_done()

    print(task.errors)
