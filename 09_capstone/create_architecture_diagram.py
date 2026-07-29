import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def add_box(ax, x, y, width, height, text):
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.03",
        linewidth=1.5,
        facecolor="white",
        edgecolor="black",
    )
    ax.add_patch(box)

    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=10,
    )


def main():
    fig, ax = plt.subplots(figsize=(14, 5))

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")

    boxes = [
        (0.3, 2, 1.7, 1, "Raw Data\nCSV / SQL"),
        (2.7, 2, 1.7, 1, "ETL Pipeline\nExtract, Transform, Load"),
        (5.1, 2, 1.7, 1, "Processed Data\nParquet / Database"),
        (7.5, 2, 1.7, 1, "Analytics\nKPIs and Insights"),
        (9.9, 3, 1.7, 1, "ML Model\nReorder Prediction"),
        (9.9, 1, 1.7, 1, "Chatbot\nBusiness Questions"),
        (12.1, 2, 1.5, 1, "Streamlit\nInterface"),
    ]

    for box in boxes:
        add_box(ax, *box)

    arrow_style = dict(arrowstyle="->", linewidth=1.5)

    ax.annotate("", xy=(2.7, 2.5), xytext=(2, 2.5), arrowprops=arrow_style)
    ax.annotate("", xy=(5.1, 2.5), xytext=(4.4, 2.5), arrowprops=arrow_style)
    ax.annotate("", xy=(7.5, 2.5), xytext=(6.8, 2.5), arrowprops=arrow_style)

    ax.annotate("", xy=(9.9, 3.5), xytext=(9.2, 2.7), arrowprops=arrow_style)
    ax.annotate("", xy=(9.9, 1.5), xytext=(9.2, 2.3), arrowprops=arrow_style)

    ax.annotate("", xy=(12.1, 2.7), xytext=(11.6, 3.3), arrowprops=arrow_style)
    ax.annotate("", xy=(12.1, 2.3), xytext=(11.6, 1.7), arrowprops=arrow_style)

    ax.set_title(
        "Customer Insights and Sales Analytics Assistant Architecture",
        fontsize=15,
        pad=20,
    )

    plt.tight_layout()
    plt.savefig(
        "09_capstone/capstone_architecture.png",
        dpi=300,
        bbox_inches="tight",
    )

    print("Architecture diagram created successfully.")


if __name__ == "__main__":
    main()
