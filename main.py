import pandas as pd
import cv2


def mark_class(row) -> int:
    """Mark for class"""
    mark = 1
    if row["class"] == "tiger":
        mark = 0
    return mark


def width(row) -> int:
    """Calculation width"""
    image = cv2.imread(row["absolute way"])
    w = image.shape[1]
    return w


def height(row) -> int:
    """Calculation height"""
    image = cv2.imread(row["absolute way"])
    h = image.shape[0]
    return h


def depth(row) -> int:
    """Calculation depth"""
    image = cv2.imread(row["absolute way"])
    d = image.shape[2]
    return d


def sort_mark(dframe, mark: int):
    """Filtering by class mark"""
    dframe = df[dframe.mark == mark]
    return dframe


if __name__ == "__main__":
    df = pd.read_csv("dataset.csv", sep=";")
    df = df.rename(columns={"Absolute way": "absolute way"})
    df = df.rename(columns={"Class": "class"})
    df = df.drop(["Relative way"], axis=1)

    df["mark"] = df.apply(mark_class, axis=1)

    df["height"] = df.apply(height, axis=1)
    df["width"] = df.apply(width, axis=1)
    df["depth"] = df.apply(depth, axis=1)
    df.describe()

    print(sort_mark(df, 0))
