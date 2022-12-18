import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("dataset.csv", sep=";")
    df = df.rename(columns={'Absolute way': 'absolute_way'})
    df = df.rename(columns={'Class': 'class'})
    df = df.drop(["Relative way"], axis=1)

    print(df)
