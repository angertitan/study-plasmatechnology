import json
from matplotlib import pyplot as plt
from os import listdir
from os.path import join, splitext


def plot_it(x, y=None, invert_xaxis=False, name='', ylabel='y', xlabel='x', figsize=(1200, 800)):

    print("creating figure for {}".format(name))

    figsize_inch = (figsize[0] / 96, figsize[1] / 96)

    fig = plt.figure(figsize=figsize_inch)
    plt.xlabel(xlabel, fontsize=12, fontweight="bold")
    plt.ylabel(ylabel, fontsize=12, fontweight="bold")
    if not y:
        plt.plot(x)
    else:
        plt.plot(x, y)
    if invert_xaxis:
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
        plot_it(data_array[0], data_array[1], name=filename, ylabel=label)


def load_data(path, lab=1):
    file = open(path)
    file_string = file.read()

    data_array = json.loads(file_string)

    if lab == 2:
        return data_array

    x_values = []
    y_values = []
    for data in data_array:
        x_values.append(float(data["wavenumber"]))
        y_values.append(float(data["value"]))

    return [x_values, y_values]


def multichart(*args, lab=2, invert_xaxis=False, name='', ylabel='', xlabel='' ):
    fig = plt.figure()
    
    plt.xlabel(xlabel, fontsize=12, fontweight="bold")
    plt.ylabel(ylabel, fontsize=12, fontweight="bold")
    
    for d in args:
        if lab == 2:
            plt.plot(d)
        else:
            plt.plot(d[0], d[1])
        
        if invert_xaxis:
            plt.gca().invert_xaxis()
        
    fig.tight_layout()
    
    plt.savefig("./charts/" + name + ".png", format="png")

