
import pandas as pd
import matplotlib.pyplot as plt

class Strain:
    def __init__(self, strain_data, background, color, label):
        strain_data -= background
        self.mu = strain_data.mean()
        self.std = strain_data.std()
        self.n = len(self.mu)
        self.color = color
        self.label = label

def get_replicates(tag, row, rm_replicates):
    df = pd.read_csv(tag+'.csv', header=None)
    for rep in rm_replicates:
        df = df[~df[0].str.contains(str(rep))]    
    return df[df[0].str.contains(str(row))]

def get_background(tag):
    df = pd.read_csv(tag+'.csv', header=None)
    return df[df[0].str.contains(str('B'))].mean()



def main():
    # read data

    ###
    #tag = 'od600'
    tag = 'gfp'
    #strain_1_data = get_replicates(tag, 10, ['A', 'B', 'H', 'G'])               # not all replicates
    strain_1_data = get_replicates(tag, 10, ['A', 'B', 'H'])                     # all replicates
    ###

    strain_2_data = get_replicates(tag, 11, ['A', 'B', 'H'])
    strain_3_data = get_replicates(tag, 8, ['A', 'B', 'H'])

    background = get_background(tag)

    # do calculations
    strain_1 = Strain(strain_1_data, background, 'blue', 'Empty Vector')
    strain_2 = Strain(strain_2_data, background, 'red', 'Wild Type sRNA')
    strain_3 = Strain(strain_3_data, background, 'green', 'Mutated sRNA-X')

    # plot
    strains = [strain_1, strain_2, strain_3]

    # plot option 1
    for strain in strains:
        plt.plot(range(strain.n), strain.mu, strain.color, label=strain.label)
        plt.fill_between(range(strain.n), strain.mu - 1*strain.std, strain.mu + 1*strain.std, alpha=0.3, color=strain.color)
        #plt.fill_between(range(strain.n), strain.mu - 2*strain.std, strain.mu + 2*strain.std, alpha=0.3, color=strain.color)

    ###
    #plt.title(f'{tag.upper()} Over Time')                                # if od600
    plt.title(f'{tag.upper()} Fluorescence Over Time')                  # if GFP
    ###

    plt.xlabel('Measurement')
    plt.ylabel(f'{tag.upper()}')
    plt.legend()

    ###
    #plt.savefig(f"{tag}_{'mean.png'}")                                    # if not all replicates
    plt.savefig(f"{tag}_all_rep_{'mean.png'}")                           # if all replicates
    ###

    plt.figure()

    


if __name__ == '__main__':
    main()


    


















    """
    # plot option 2
    for strain in strains:
        plt.plot(range(strain.n), strain.mu, strain.color)
    plt.savefig(f"{tag}_{'mu.png'}")
    plt.figure()

    for strain in strains:
        plt.plot(range(strain.n), strain.std, strain.color)
    plt.savefig(f"{tag}_{'std.png'}")
    plt.figure()
    """

