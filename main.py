import time 
import csv 
import pandas as pd 

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
duration = time_convert(time_lapsed)

df =pd.read_csv('data.csv')
df = pd.DataFrame(df)

data = {start_time, end_time , duration}


header = ['start_time ', 'end_time ', 'duration ']

data = dict(zip(('start_time ', 'end_time ', 'duration '),(start_time, end_time, time_lapsed)))
with open('data.csv', 'a') as f:
    writer = csv.DictWriter(f, fieldnames= header)

    writer.writerow(data)

    f.close()


