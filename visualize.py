import json
from matplotlib import pyplot as plt
from os import listdir
from os.path import join, splitext


def original_to_chart(data_array, name, ylabel, figsize=(1200, 800)):

    print("creating figure for {}".format(name))

    figsize_inch = (figsize[0] / 96, figsize[1] / 96)

    fig = plt.figure(figsize=figsize_inch)
    plt.xlabel("Wellenzahl", fontsize=12, fontweight="bold")
    plt.ylabel(ylabel, fontsize=12, fontweight="bold")
    plt.plot(data_array[0], data_array[1])
    plt.gca().invert_xaxis()
    # plt.ylim(0, 1)
    fig.tight_layout()

    plt.savefig("./charts/" + splitext(name)[0] + ".png", format="png")
    # plt.show()


def visualize_many(dirname):
    files = listdir(dirname)

    label = ""
    for filename in files:
        if filename == "Gruppe3.0.json" or filename == "Gruppe3.3.json":
            label = "Intensität"
        else:
            label = "Quotient"

        data_array = load_data(join(dirname, filename))
        original_to_chart(data_array, filename, label)


def load_data(path):
    file = open(path)
    file_string = file.read()

    data_array = json.loads(file_string)

    x_values = []
    y_values = []
    for data in data_array:
        x_values.append(float(data["wavenumber"]))
        y_values.append(float(data["value"]))

    return [x_values, y_values]


def multichart(data1, data2, name):
    fig = plt.figure()
    
    plt.xlabel("Wellenzahl", fontsize=12, fontweight="bold")
    plt.ylabel("Quotient", fontsize=12, fontweight="bold")
    
    plt.plot(data1[0], data1[1])
    plt.gca().invert_xaxis()
    
    plt.plot(data2[0], data2[1], 'g')
    #plt.gca().invert_xaxis()
    
    fig.tight_layout()
    
    plt.savefig("./charts/" + name + ".png", format="png")

#visualize_many("data/parsed")
data1 = load_data('data/parsed/Gruppe3.15.json')
data2 = load_data('data/parsed/Gruppe3.16.json')

data3 = load_data('data/parsed/Gruppe3.4.json')
data4 = load_data('data/parsed/Gruppe3.12.json')


multichart(data2, data1, '3.15_3.16')
multichart(data4, data3, '3.4_3.12')


