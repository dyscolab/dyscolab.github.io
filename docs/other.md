---
hide:
  - navigation
---
# Other libraries
Aside from the main 3 user facing libraries, Dyscolab mantains a number of other auxiliary and related ones:

- [symbolite](https://github.com/dyscolab/symbolite): a minimalist symbolic python package used by Poincare, SimBio and Jablonski.
- [numbakit-ode](https://github.com/dyscolab/numbakit-ode): python implementation of different ODE integration methods using [numba](https://numba.pydata.org/) to speed up calculations.
- [scipy-events](https://github.com/dyscolab/scipy-events): functionality to listen for events during ODE integration in `scipy.integrate.solve_ivp`, used in `poincare.SteadyState`.
- [numbakit-anjit](https://github.com/dyscolab/numbakit-anjit): an annotation aware numba jit decorator and manager object to handle Jit configuration.
- [biomodels](https://github.com/dyscolab/biomodels): a python library to download models from [BioModels](https://www.ebi.ac.uk/biomodels/).