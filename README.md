# ClusterCSV2NOA
# Language: Python
# Input: CSV (clusters)
# Output: NOA (nodes and cluster ID)
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin that converts a file of nodes and clusters in CSV format into
a NOde Attribute (NOA) file for Cytoscape (Shannon et al, 2003).

The clusters file should be in the following format:

"","x"
"1","Family.Lachnospiraceae.0001"
"2","Family.Ruminococcaceae.0003"
"3","Family.Lachnospiraceae.0029"
"4","Family.Lachnospiraceae.0043"
"5","Family.Ruminococcaceae.0019"
"6","Family.Lachnospiraceae.0095"
"","x"
"1","Family.Porphyromonadaceae.0005"
"2","Family.Porphyromonadaceae.0006"
"3","Family.Lachnospiraceae.0045"
"4","Order.Clostridiales.0007"
"","x"
"1","Kingdom.Bacteria.0001"
"2","Family.Porphyromonadaceae.0013"
"3","Phylum.Firmicutes.0004"

The output NOA file will be in the following simple table format:

Name	Cluster
Family.Lachnospiraceae.0001	1
Family.Ruminococcaceae.0003	1
Family.Lachnospiraceae.0029	1
Family.Lachnospiraceae.0043	1
Family.Ruminococcaceae.0019	1
Family.Lachnospiraceae.0095	1
Family.Porphyromonadaceae.0005	2
Family.Porphyromonadaceae.0006	2
Family.Lachnospiraceae.0045	2
Order.Clostridiales.0007	2
Kingdom.Bacteria.0001	3
Family.Porphyromonadaceae.0013	3
Phylum.Firmicutes.0004	3

This file can in turn be imported into Cytoscape, and the cluster number
can be assigned to each node as an attribute for downstream analysis or visualization.
