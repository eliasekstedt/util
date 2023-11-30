
import pandas as pd
import matplotlib.pyplot as plt

class Strain:
    def __init__(self, strain_data, color):
        self.mu = strain_data.mean()
        self.std = strain_data.std()
        self.n = len(self.mu)
        self.color = color

def get_replicates(row):
    df = pd.read_csv('file.csv')
    return df[df['Well'].str.contains(str(row))]


def main():
    # read data
    df = pd.read_csv('file.csv')

    strain_1_data = get_replicates(10)
    strain_2_data = get_replicates(11)
    strain_3_data = get_replicates(8)

    # do calculations
    strain_1 = Strain(strain_1_data, color='blue')
    strain_2 = Strain(strain_2_data, color='red')
    strain_3 = Strain(strain_3_data, color='green')
    
    # plot
    strains = [strain_1, strain_2, strain_3]

    # plot option 1
    for strain in strains:
        plt.plot(range(strain.n), strain.mu, strain.color)
        plt.fill_between(range(strain.n), strain.mu - 1*strain.std, strain.mu + 1*strain.std, alpha=0.3, color=strain.color)
        plt.fill_between(range(strain.n), strain.mu - 2*strain.std, strain.mu + 2*strain.std, alpha=0.3, color=strain.color)
    plt.savefig('mu_&_std.png')
    plt.figure()

    # plot option 2
    for strain in strains:
        plt.plot(range(strain.n), strain.mu, strain.color)
    plt.savefig('mu.png')
    plt.figure()

    for strain in strains:
        plt.plot(range(strain.n), strain.std, strain.color)
    plt.savefig('std.png')
    plt.figure()

    print(strain_1.mu)
    print(strain_1.std)

if __name__ == '__main__':
    main()


    