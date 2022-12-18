import pandas as pd


def mark_class(row) -> int:
    mark = 1
    if row["class"] == "tiger":
        mark = 0
    return mark


if __name__ == "__main__":
    df = pd.read_csv("dataset.csv", sep=";")
    df = df.rename(columns={"Absolute way": "absolute_way"})
    df = df.rename(columns={"Class": "class"})
    df = df.drop(["Relative way"], axis=1)

    df["mark"] = df.apply(mark_class, axis=1)

    print(df)
