import process_input
import matplotlib.pyplot as plt
import csv

def plot_data(input_file_path):
    plt.plotfile(input_file_path, delimiter=';', cols=(0, 1, 2, 3), subplots=False)
    plt.show()


def step_detector(input_file_path):
    # plot data
    #plot_data(input_file_path)

    # read data from csv
    with open(input_file_path) as data_file:
        data = csv.DictReader(data_file, delimiter=';')

        timestamps = []
        x_values = []
        y_values = []
        z_values = []

        for row in data:
            timestamps.append(row['timestamp'])
            x_values.append(row['x'])
            y_values.append(row['y'])
            z_values.append(row['z'])

        timestamps = timestamps[500:1000]
        x_values = x_values[500:1000]
        y_values = y_values[500:1000]
        z_values = z_values[500:1000]

        steps_count = 0

        last_extremum_value = float(z_values[0])
        last_extremum_position = 0
        direction = 1  # 1 = peak, 0 = valley

        average_peak_value = 0
        peak_count = 0
        peak_timestamps = []
        peak_average_values = []

        average_valley_value = 0
        valley_count = 0
        valley_timestamps = []
        valley_average_values = []

        acc_threshold = 17
        time_difference = 0.2

        for i in range(1, len(z_values)):
            val = float(z_values[i])
            if direction == 1:
                if last_extremum_value > val:
                    # a valley seems to come, check weather the difference is sufficient

                    print last_extremum_value, val, abs(last_extremum_value - val)

                    if abs(last_extremum_value - val) > acc_threshold \
                            and abs(float(timestamps[last_extremum_position]) - float(timestamps[i])) > time_difference:

                        direction = 0
                        steps_count += 1

                        # update the average_peak_value
                        average_peak_value = (last_extremum_value + average_peak_value * peak_count) / (peak_count + 1)
                        peak_count += 1
                        peak_average_values.append(average_peak_value)

                        # save the timestamp where the peak was seen
                        peak_timestamps.append(timestamps[last_extremum_position])

                        last_extremum_value = val
                        last_extremum_position = i

                if last_extremum_value < val:
                    # just update the extremum, we have a value that will lead to a higher peak
                    last_extremum_value = val
                    last_extremum_position = i

            if 0 == direction:
                if last_extremum_value < val:
                    # a peak seems to come, check weather the difference is sufficient

                    print last_extremum_value, val, abs(last_extremum_value - val)

                    if abs(last_extremum_value - val) > acc_threshold \
                            and abs(float(timestamps[last_extremum_position]) - float(timestamps[i])) > time_difference:

                        direction = 1
                        steps_count += 1

                        # update the average_valley_value
                        average_valley_value = (last_extremum_value + average_valley_value * valley_count) / (valley_count + 1)
                        valley_count += 1
                        valley_average_values.append(average_valley_value)

                        # save the timestamp where the valley was seen
                        valley_timestamps.append(timestamps[last_extremum_position])

                        last_extremum_value = val
                        last_extremum_position = i

                if last_extremum_value > val:
                    # just update the extremum, we have a value that will lead to a lower valley
                    last_extremum_value = val
                    last_extremum_position = i

            # print direction, last_extremum_value, last_extremum_position

    print 'Avg Peak: ', average_peak_value
    print 'Avg Valley: ', average_valley_value
    print '#Peaks: ', peak_count
    print '#Valleys:', valley_count

    print 'Peak timestamps: ', peak_timestamps
    print 'Valley timestamps: ', valley_timestamps

    print 'Peak averages: ', peak_average_values
    print 'Valley averages: ', valley_average_values

    return steps_count

# Process the input
process_input.process_file('/home/virgil/workspace/PycharmProjects/step_detector/Data/LinearAccelerationDataFile_2016_02_22__09_06_48.txt')
# Run function
no_of_steps = step_detector('/home/virgil/workspace/PycharmProjects/step_detector/Data/LinearAccelerationDataFile_2016_02_22__09_06_48.csv')
print(no_of_steps / 2)

# Process the input
#process_input.process_file('/home/virgil/workspace/PycharmProjects/step_detector/Data/LinearAccelerationDataFile_2016_03_28__16_22_43.txt')
# Run function
#no_of_steps = step_detector('/home/virgil/workspace/PycharmProjects/step_detector/Data/LinearAccelerationDataFile_2016_03_28__16_22_43.csv')
#print(no_of_steps)