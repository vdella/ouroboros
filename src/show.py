from tabulate import tabulate


def show(results):
    headers = ['Algorithm', 'Number size', 'Generation time', 'Miller-Rabin', 'Fermat']
    print(tabulate(results, headers=headers, tablefmt='fancy_grid'))
