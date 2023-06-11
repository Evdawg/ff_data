import nfl_data_py as nfl
import pandas as pd

schedule_2023 = nfl.import_schedules([2023])

sched_df = pd.DataFrame(schedule_2023)
nfl.clean_nfl_data(sched_df)
print(sched_df)

sched_df.to_csv('test.csv', index= False)