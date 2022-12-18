import pandas as pd
import cv2
import matplotlib.pyplot as plt
import random


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


def sort_par(dframe, mark, max_height, max_width):
    """Create new dataframe filtered by mark and size"""
    dframe = df[(dframe.mark == mark) & (dframe.height <= max_height) & (dframe.width <= max_width)]
    return dframe


def histogram(dframe, mark: int) -> tuple:
    """Histogram"""
    dfr = sort_mark(dframe, mark)
    list1 = []
    list2 = []
    list3 = []
    for index in dfr.index:
        image = cv2.imread(dfr["absolute way"].loc[dfr.index[index]])
        list1.append(cv2.calcHist([image], [0], None, [256], [0, 256]))
        list2.append(cv2.calcHist([image], [1], None, [256], [0, 256]))
        list3.append(cv2.calcHist([image], [2], None, [256], [0, 256]))
    return list1, list2, list3


if __name__ == "__main__":
    df = pd.read_csv("dataset.csv", sep=";")
    df = df.rename(columns={"Absolute way": "absolute way"})
    df = df.rename(columns={"Class": "class"})
    df = df.drop(["Relative way"], axis=1)
    print("\033[32m{}\033[0m".format("DataFrame"))
    print(df)

    df["mark"] = df.apply(mark_class, axis=1)
    print("\033[32m{}\033[0m".format("DataFrame with mark"))
    print(df)

    df["height"] = df.apply(height, axis=1)
    df["width"] = df.apply(width, axis=1)
    df["depth"] = df.apply(depth, axis=1)
    print("\033[32m{}\033[0m".format("DataFrame with size"))
    print(df)

    st = df.describe()
    print("\033[32m{}\033[0m".format("Statistics"))
    print(st)

    s_mark = sort_mark(df, 0)
    print("\033[32m{}\033[0m".format("Sorted by mark"))
    print(s_mark)
    s_par = sort_par(df, 1, 300, 480)
    print("\033[32m{}\033[0m".format("Sorted by size"))
    print(s_par)

    df["size"] = df["height"] * df["width"] * df["depth"]
    result = df.groupby("mark").agg({"size": ["mean", "min", "max"]})
    print("\033[32m{}\033[0m".format("Max filter"))
    print(result)

    h_1, h_2, h_3 = histogram(df, 0)
    i = random.randint(0, 1100)
    num = str(i)
    plt.plot(h_1[i], color="blue")
    plt.xlim([0, 256])
    plt.plot(h_2[i], color="green")
    plt.xlim([0, 256])
    plt.plot(h_3[i], color="red")
    plt.xlim([0, 256])
    plt.title("Histogram image No." + num)
    plt.ylabel("Pixel value")
    plt.xlabel("Count")
    plt.show()
