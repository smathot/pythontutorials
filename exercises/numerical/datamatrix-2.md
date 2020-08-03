This is a challenging exercise!

Download [this dataset](/data/zhou_et_al_2020_exp1.csv) from Zhou et al. (2020) and read it with datamatrix. This dataset contains reaction times on a search task (`search_rt`) for different participants (`subject_nr`). Each row in this dataset corresponds to a single response, i.e. it is unaggregated data. 

The goal of this exercise is to remove all data from those participants whose mean reaction time deviates more than two standard deviations from the grand mean reaction time. Here, both the standard deviation and the grand mean are derived from per-participant mean reaction times (i.e. a mean-of-means approach). 

Hints:

- You first need to create a datamatrix with the mean reaction time for each participant.
- The function `datamatrix.operations.group()` groups a datamatrix based on a column, in this case `subject_nr`. The resulting datamatrix will contain a `search_rt` column for each subject, where each cell contains multiple values (i.e. multiple reaction times).
- You can use `datamatrix.series.reduce_()` to get the mean reaction time for each subject.
