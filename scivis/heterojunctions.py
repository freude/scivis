import numpy as np
import matplotlib.pyplot as plt


def show_edges(data):
    num_of_struct = len(edges)
    num_of_elements = 3 * num_of_struct - 1
    cursor = 0
    step = 10
    coords = []

    ax = plt.gca()

    for j, item in enumerate(edges):
        print(j)
        if j != 0:
            cursor += step

        plt.plot([cursor, cursor + step], [item['ev1'], item['ev1']], '#F39C12', linewidth=5.0)
        plt.plot([cursor, cursor + step], [item['ec1'], item['ec1']], '#3498DB', linewidth=5.0)
        plt.plot([cursor + step, cursor + 2 * step], [item['ev2'], item['ev2']], '#F39C12', linewidth=5.0)
        plt.plot([cursor + step, cursor + 2 * step], [item['ec2'], item['ec2']], '#3498DB', linewidth=5.0)

        cb = item['ec2'] - item['ec1']
        vb = item['ev2'] - item['ev1']

        plt.plot([cursor + step, cursor + step], [item['ec1'], item['ec1'] + cb], '#3498DB', linewidth=2.0)
        plt.plot([cursor + step, cursor + step], [item['ev1'], item['ev1'] + vb], '#F39C12', linewidth=2.0)

        plt.text(cursor + 1, item['ev1'] + 0.1, str(item['ev1']))
        plt.text(cursor + 1, item['ec1'] + 0.1, str(item['ec1']))
        plt.text(cursor + step + 2, item['ev2'] + 0.1, str(item['ev2']))
        plt.text(cursor + step + 2, item['ec2'] + 0.1, str(item['ec2']))

        coords.append(cursor + step)
        cursor += 2 * step

    ax.tick_params(direction='in')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    plt.xticks(coords, np.arange(num_of_struct))
    plt.ylabel('Energy (eV)')
    plt.show()


if __name__ == '__main__':

    edges= [{'ev1': 0.0, 'ec1': 1.0, 'ev2': 0.5, 'ec2': 1.5},
            {'ev1': -1.0, 'ec1': 2.0, 'ev2': 0.0, 'ec2': 1.0},
            {'ev1': 2.0, 'ec1': 3.0, 'ev2': 1.0, 'ec2': 3.0},
            {'ev1': 0.0, 'ec1': 1.0, 'ev2': 0.0, 'ec2': 1.0},
            ]

    show_edges(edges)

