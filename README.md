# Pileup weight derivation

```cpp
n_TrueInt = fs->make<TH1D>("n_TrueInt", "n_TrueInt", 99, 0, 99); # and just fill per event
```

## Usage

1. Make a bunch of `.json`s, one for each dataset:
```bash
python3 make_specs.py
```
2. Make the files that have the TH1D's of the true pileup:
```bash
python3 get_pileup_distributions.py
```
This makes files `nTrueInt_*.root` in the `outputFiles/` directory.

3. Use the outputs of step 1 to make the weights.
```bash
bash make_weight.sh
```