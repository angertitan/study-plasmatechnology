import json
from matplotlib import pyplot as plt
from os import listdir
from os.path import join


def original_to_chart(data_array, name, figsize=(1200, 800)):

    print('creating figure for {}'.format(name))

    plt.xlabel = ("Wellenzahl [1/cm]")
    plt.ylabel = ("Absorbtionsgrad [I0/I]")
    plt.plot(data_array[0], data_array[1])
    # fig.tight_layout()
    #plt.savefig('./charts/' + name + '.png', format="png")
    plt.show()


def visualize_many(dirname):
    files = listdir(dirname)

    for filename in files:
        data_array = load_data(join(dirname, filename))
        original_to_chart(data_array, filename)


def load_data(path):
    file = open(path)
    file_string = file.read()

    data_array = json.loads(file_string)

    x_values = []
    y_values = []
    for data in data_array:
        x_values.append(float(data['wavenumber']))
        y_values.append(float(data['value']))

    return [x_values, y_values]


#visualize_many('data/parsed')
test = load_data('data/parsed/Gruppe3.0.json')
