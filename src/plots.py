import matplotlib.pyplot as plt
import numpy as np
import os

# ensure plots folder exists
os.makedirs("plots", exist_ok=True)

# 1. Line plot
def line_plot(df):
    plt.figure(figsize=(8,5))
    plt.plot(df["date"], df["sales"], marker='o')
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig("plots/line_plot.png", dpi=300)
    plt.show()


# 2. Bar plot
def bar_plot(region_sales):
    plt.figure()
    region_sales.plot(kind="bar", color="skyblue")
    plt.title("Sales by Region")
    plt.savefig("plots/bar_plot.png", dpi=300)
    plt.show()


# 3. Histogram
def histogram(df):
    plt.figure()
    plt.hist(df["sales"], bins=5, edgecolor='black')
    plt.title("Sales Distribution")
    plt.savefig("plots/histogram.png", dpi=300)
    plt.show()


# 4. Scatter plot
def scatter_plot(df):
    plt.figure()
    plt.scatter(df["sales"], df["profit"], c=df["profit"], cmap="viridis")
    plt.colorbar(label="Profit")
    plt.title("Sales vs Profit")
    plt.savefig("plots/scatter.png", dpi=300)
    plt.show()


# 5. Subplots
def subplots(df):
    fig, axs = plt.subplots(2,2, figsize=(10,8))

    axs[0,0].plot(df["sales"])
    axs[0,0].set_title("Sales Trend")

    axs[0,1].hist(df["profit"])
    axs[0,1].set_title("Profit Distribution")

    axs[1,0].scatter(df["sales"], df["profit"])
    axs[1,0].set_title("Scatter")

    axs[1,1].plot(df["profit"], color='red')
    axs[1,1].set_title("Profit Trend")

    plt.tight_layout()
    plt.savefig("plots/subplots.png", dpi=300)
    plt.show()


# 6. Heatmap
def heatmap(df):
    corr = df[["sales","profit"]].corr()

    plt.figure()
    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns)
    plt.yticks(range(len(corr)), corr.columns)

    for i in range(len(corr)):
        for j in range(len(corr)):
            plt.text(j, i, round(corr.iloc[i,j],2),
                     ha="center", va="center")

    plt.title("Correlation Heatmap")
    plt.savefig("plots/heatmap.png", dpi=300)
    plt.show()


# 7. Annotation
def annotated_plot(df):
    plt.figure()
    plt.plot(df["sales"])
    max_idx = np.argmax(df["sales"])

    plt.annotate("Peak",
                 (max_idx, df["sales"][max_idx]),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

    plt.title("Annotated Peak")
    plt.savefig("plots/annotated.png", dpi=300)
    plt.show()