library(ggraph)
library(igraph)

drugs <- read.csv("drug_combos.csv", header=TRUE)
graph <- graph_from_data_frame(drugs)

layout <- create_layout(graph = graph, layout = "linear", circular = FALSE)
ggraph(layout) + 
  geom_edge_arc(aes(colour = factor(CohortText))) + 
  geom_node_point()



