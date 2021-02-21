with open('samll_data.csv', 'r') as f_in, open('weather_small.csv', 'w') as f_out:
    f_out.write(next(f_in))
    [f_out.write(','.join(line.split()) + '\n') for line in f_in]