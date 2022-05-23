library(UpSetR)


movies <- read.csv(system.file("extdata", "movies.csv", package = "UpSetR"), header = T, sep = ";")

drugs <- read.csv("direct_drugs.csv", header=TRUE)

# drugs$cohort_new <- as.factor(drugs$cohort_new)

CohortCapture <- function(row, cohort) {
  data <- (row["cohort_new"] == cohort)
}


upset(
  drugs, 
  nsets = 8,  # we only have 17 drugs
  order.by = "freq",
  mb.ratio = c(0.60, 0.40),  # plot area , intersection area
  nintersects = 56,  # number of intersections
  # cutoff = 1,  
  # number.angles = 45,
  group.by = "sets",
  cutoff = 7,
  mainbar.y.label = "Drug Combination Intersections", 
  sets.x.label = "Drug Names", 
  queries = list(
    list(
      query = CohortCapture, params = 1, color = "blue", active = F, query.name = "Stimulant"
    ),
    list(
      query = CohortCapture, params = 2, color = "red", active = F, query.name = "Opioid"
    ),
    list(
      query = CohortCapture, params = 3, color = "orange", active = T, query.name = "Both"
    )
  )
)


