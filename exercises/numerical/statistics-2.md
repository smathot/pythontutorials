- Read [this dataset](/data/fmri-data.npy), which has been adapted from the [StudyForrest](http://studyforrest.org/) project. See Exercise 2 from the [NumPy tutorial](%url:numpy%) if you don't remember this dataset!
- Get the mean BOLD response over time, separately for the left and the right brain.
- Plot the BOLD response over time for the left and the right brain.
- You will notice that there is a slight drift in the signal, such that the BOLD response globally increases over time. You can remove this with so-called detrending, using `scipy.signal.detrend()`.
- Plot the detrended BOLD response over time for the left and the right brain.
- Determine the correlation between the detrended BOLD response in the left and the right brain.

Statistical caveat: Measures that evolve over time, such as the BOLD response, are not independent. Therefore, statistical tests that assume independent observations are invalid for this kind of data! In this exercise, this means that the p-value for the correlation is not meaningful.
