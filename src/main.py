import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def run(config):

    datasetName = config.dataset

    path_to_edgelist = os.path.join(
        os.path.dirname(os.getcwd()), "Networks/" + datasetName + "/out." + datasetName
    )

    G = nx.read_edgelist(path=path_to_edgelist)
    # with open(path_to_edgelist, "rt") as f:
    #     H = nx.parse_edgelist(f, create_using=nx.DiGraph())

    b = nx.betweenness_centrality(G)
    d = nx.degree_centrality(G)
    c = nx.closeness_centrality(G)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    # fig.figsize((90, 50))
    fig.suptitle(f"Example plots for {datasetName}")

    ### subplot 1
    L = nx.normalized_laplacian_matrix(G)
    e = np.linalg.eigvals(L.A)
    ax1.hist(e, bins=100)  # histogram with 100 bins
    ax1.set_title("Eigenvalue histogram")
    ax1.set_xlabel("eigenvalue")

    ### subplot 2
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    # print "Degree sequence", degree_sequence
    dmax = max(degree_sequence)

    ax2.loglog(degree_sequence, "b-", marker="o")
    ax2.set_title("Degree vs Rank plot")
    ax2.set_ylabel("Degree")
    ax2.set_xlabel("Rank")

    ### subplot 3
    ax3.hist(nx.clustering(G).values(), bins=100)
    ax3.set_title("Clustering histogram")
    ax3.set_xlabel("Clustering Co-efficient")

    ### subplot 4
    # Raw Graph

    ax4.set_title("Raw Graph")
    ax4 = nx.draw_networkx(G)

    print()
    print("Average betweenness_centrality = ", sum(b.values()) / len(b))
    print("Average degree_centrality = ", sum(d.values()) / len(d))
    print("Average closeness_centrality = ", sum(c.values()) / len(c))
    print()
    print("Largest eigenvalue:", max(e))
    print("Smallest eigenvalue:", min(e))
    print(config.plot)

    if config.plot == True:
        plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Take in dataset name and plot option, mainly for example purposes"
    )
    parser.add_argument(
        "dataset", type=str, help="Name of Konect dataset, as is in downloaded file",
    )
    parser.add_argument(
        "--plot", default=True, help="Whether to plot or not, default True",
    )

    config = parser.parse_args()

    run(config)

