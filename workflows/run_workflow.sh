python open_data.py ../data/data_03_04_12_t12.mat --save ../results/corr.npz --bin-size 20.
python plot_correlations_histogram.py ../results/corr.npz --save-fig ../figures/corr.png
