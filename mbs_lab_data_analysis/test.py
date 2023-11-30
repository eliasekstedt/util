
import pandas as pd


def get_replicates(row):
    df = pd.read_csv('file.csv')
    return df[df['Well'].str.contains('8')]






def main():
    print(get_replicates(8))



if __name__ == '__main__':
    main()






