import numpy as np
import matplotlib.pyplot as plt


def show_edges(data,
               ax=None,
               width=10,
               lw=5.0,
               spacing=10.0,
               show_labels=True,
               colors=('#F39C12', '#3498DB'),
               ticks=[]):
    """
    Plot band edges for a set of heterojunctions

    Parameters
    ----------
    data : list of dictionaries
        List of band edges for heterostructures in the following format
            [{'ev1': 0.0, 'ec1': 1.0, 'ev2': 0.5, 'ec2': 1.5},
             {'ev1': -1.0, 'ec1': 2.0, 'ev2': 0.0, 'ec2': 1.0},
             {'ev1': 2.0, 'ec1': 3.0, 'ev2': 1.0, 'ec2': 3.0},
             {'ev1': 0.0, 'ec1': 1.0, 'ev2': 0.0, 'ec2': 1.0},
            ]
        where ev1 and ec1 is the valence and conduction band edge for
              the left contact;
              ev2 and ec2 is the valence and conduction band edge for
              the right contact;

    ax : matplotlib.pyplot.axis, optional
        Axis to plot in, if None the script will create a new one
    width : float, optional
        Width of the markers denoting the band edges
    lw : float, optional
        Height of the markers denoting the band edges
    spacing : float, optional
        Spacing between pairs of band edges
    show_labels : bool, optional
        If True shows numerical values of the band edges (in eV).
    colors : tuple, optional
        Tuple of two elements with values of colors for
        the valence and conduction bands respectivelly
    ticks : list, optional
        List of labels for the x-axis denoting heterojunctions.
    """

    num_of_struct = len(edges)
    step = width
    cursor = 0
    coords = []

    if ax is None:
        ax = plt.gca()

    if len(ticks) == 0:
        ticks = np.arange(num_of_struct)

    for j, item in enumerate(edges):
        print(j)
        if j != 0:
            cursor += spacing

        plt.plot([cursor, cursor + step],
                 [item['ev1'], item['ev1']], colors[0], linewidth=lw)
        plt.plot([cursor, cursor + step],
                 [item['ec1'], item['ec1']], colors[1], linewidth=lw)
        plt.plot([cursor + step, cursor + 2 * step],
                 [item['ev2'], item['ev2']], colors[0], linewidth=lw)
        plt.plot([cursor + step, cursor + 2 * step],
                 [item['ec2'], item['ec2']], colors[1], linewidth=lw)

        cb = item['ec2'] - item['ec1']
        vb = item['ev2'] - item['ev1']

        plt.plot([cursor + step, cursor + step],
                 [item['ec1'], item['ec1'] + cb], colors[1], linewidth=2.0)
        plt.plot([cursor + step, cursor + step],
                 [item['ev1'], item['ev1'] + vb], colors[0], linewidth=2.0)

        if show_labels:
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
    plt.xticks(coords, ticks)
    plt.ylabel('Energy (eV)')
    plt.show()


if __name__ == '__main__':

    edges = [{'ev1': 0.0, 'ec1': 1.0, 'ev2': 0.5, 'ec2': 1.5},
             {'ev1': -1.0, 'ec1': 2.0, 'ev2': 0.0, 'ec2': 1.0},
             {'ev1': 2.0, 'ec1': 3.0, 'ev2': 1.0, 'ec2': 3.0},
             {'ev1': 0.0, 'ec1': 1.0, 'ev2': 0.0, 'ec2': 1.0},
             ]

    show_edges(edges)
