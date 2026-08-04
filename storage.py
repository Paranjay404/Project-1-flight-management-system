import csv
import os


def create_file(file_name,file_header):
    if not os.path.exists(file_name):
        with open(file_name,"w") as f:
            writer = csv.writer(f)
            writer.writerow(file_header)

def read_file(file_name):
    try:
        records = []
        with open(file_name,"r") as f:
            reader=csv.reader(f)
            next(reader)
            for row in reader:
                records.append(row)
        return records
    except:
        input("------------------------------------------AN ERROR OCCURRED, PLEASE TRY AGAIN------------------------------------------")
        return []


# in storage,py write a function that accepts a filename  
# and records in parameter and appends in the specified file

def append_record(file_name,record):
    with open(file_name,"a") as f:
        writer = csv.writer(f)
        writer.writerow(record)


def write_records(filename, header, records):
    """
    Rewrite the complete CSV file.
    Used for update and delete operations.
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for record in records:
            writer.writerow(record)
        f.close()


