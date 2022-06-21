from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Tiltmeter data
ds = pd.read_csv('data/JZtest1AM.csv').to_xarray()

# Experiment parameters
start_times = [
    datetime(2022, 6, 16, 15, 26),
    datetime(2022, 6, 16, 15, 30),
    datetime(2022, 6, 16, 15, 35),
    datetime(2022, 6, 16, 15, 40),
    datetime(2022, 6, 16, 15, 45),
]

frequencies = [0.5, 0.5, 0.75, 1, 0.75]
amplitudes = [0.08, 0.08, 0.1, 0.1, 0.1]
angles = [0, 15, 0, -15, 0]

# Format time into an array of datetimes
time = [datetime.strptime(str(t.values) + '000', '%Y-%m-%dT%H:%M:%S.%f') \
    for t in ds['ISO 8601 Time']]
time = np.array(time)

# Plot all accelerations
fig = plt.figure(figsize=(8, 6))
for v in ['Ax (g)', 'Ay (g)', 'Az (g)']:
    plt.plot(time, np.array(ds[v]), lw=1, label=v)
plt.legend()
plt.xlabel('Time [UTC]')
plt.ylabel('Acceleration (g)')
plt.grid()
plt.savefig('accel.png', dpi=200)
plt.close()

# Plot all accelerations, one per run
for n, start_time in enumerate(start_times):
    print(n, start_time)

    end_time = start_time + timedelta(seconds=120)
    run_time = (time >= start_time) & (time <= end_time)

    fig = plt.figure(figsize=(8, 6))
    for v in ['Ax (g)', 'Ay (g)', 'Az (g)']:
        plt.plot(time[run_time], np.array(ds[v][run_time]), lw=1, label=v)
    plt.legend()
    plt.xlabel('Time [UTC]')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.title('Run %i' % (n + 1) + ', f = %.2f Hz' % frequencies[n] + ', a = %.2f m' % amplitudes[n])
    plt.savefig('accel_run%i.png' % (n + 1), dpi=200)
    plt.close()

