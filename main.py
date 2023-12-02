import time
import webbrowser
import random
import json


def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)


def generate_noise(columns, noise_value):
    noise = [0] * columns
    for i in range(len(noise)):
        noise[i] = random.randint(0, noise_value)
    return noise


def generate_data(columns, rows, noise_value):
    data = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        data[i] = generate_noise(columns, noise_value)
    return data


def normalize_value_to_color_range(value, min_value, max_value, color_range):
    normalized_value = (value - min_value) / (max_value - min_value)
    index = round(normalized_value * (len(color_range) - 1))
    return color_range[index]


def generate_html(data):
    with open('index.html', 'w') as f:
        f.write('<html><head><style>body {font-family: "Ubuntu Regular", '
                'sans-serif;}</style></head><body><center><h1>Lapis\' Noise Generator</h1><table>')
        for row in data:
            f.write('<tr>')
            for col in row:
                f.write('<td style="background-color: {}; color: #ffffff; font-family: \'Ubuntu Regular\', '
                        'sans-serif;">{}</td>'.format(col[1], col[0]))
            f.write('</tr>')
        f.write('</table></center></body></html>')



def main():
    config = load_config()
    data = generate_data(config['cols'], config['rows'], config['noise_value'])
    color_data = []

    for row in data:
        row_data = []
        for col in row:
            noise_color_value = normalize_value_to_color_range(col, min(row), max(row), config['colors'])
            row_data.append((col, noise_color_value))
        color_data.append(row_data)

    generate_html(color_data)

    for i in range(5):
        print('\rOpening browser in {} seconds'.format(5 - i), end='')
        time.sleep(1)
    print()
    webbrowser.open('index.html')


if __name__ == '__main__':
    main()