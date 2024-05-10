# Pileup weight derivation

```cpp
n_TrueInt = fs->make<TH1D>("n_TrueInt", "n_TrueInt", 99, 0, 99); # and just fill per event
```

## Usage

1. Make a bunch of `.json`s, one for each dataset (in this file `make_specs.py`, edit the `datasets_to_do` array. `2018` is the year, the next thing is whatever short-hand name you want to use for the dataset, and the third thing is the DAS dataset path).
```bash
python3 make_specs.py
```
2. Make the files that have the TH1D's of the true pileup (in this file `get_pileup_distributions.py`, the loop should be over the short-hand names you specified in the previous step).
```bash
python3 get_pileup_distributions.py
```
This makes files `nTrueInt_*.root` in the `outputFiles/` directory.

3. Use the outputs of step 1 to make the weights (in this file `make_weight.sh`, the bash `for` loop should be over the short-hand names, separated with a space).
```bash
bash make_weight.sh
```