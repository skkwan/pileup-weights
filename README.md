# Pileup weight derivation

```cpp
n_TrueInt = fs->make<TH1D>("n_TrueInt", "n_TrueInt", 99, 0, 99); # and just fill per event
```

## Usage

1. Make the files that have the TH1D's of the true pileup:
```bash
# First add a .json file that lists the files in the dataset
python3 get_pileup_distributions.py
```
This makes files `nTrueInt_*.root` in the same directory.

2. Use the outputs of step 1 to make the weights.

```bash
bash make_weight.sh
```