# 2-Fuel Kinetic Model Simulation

This project provides a Python implementation of a kinetic model for simulating diacid kinetics without catalysis, involving two competing fuels. The model is implemented in the `Boek_2fuels.py` file and uses the `kinmodel` package for simulation.

## Installation

 **Install the `kinmodel` Package (https://github.com/scotthartley/kinmodel)**:
- Download the `kinmodel-4.12.1.tar.gz` file.
- Open a terminal, navigate to the folder containing the `.tar.gz` file, and run:
  ```bash
  pip install kinmodel-4.12.1.tar.gz
  ```

## Usage

To simulate the model, use the `model_kinetics` command provided by the `kinmodel` package. The simulation parameters and their order are defined in the `kinmodel.py` file.

### Parameter Order

The parameters are ordered as follows:
- **Rate Constants**: `k1_1`, `k1_2`, `K1`, `K2`, `k2`, `k0_1`, `k0_2`
- **Concentrations**: `Ac`, `F1`, `F2`, `W1`, `W2`, `An`

### Parameter Descriptions

- `k1_1`: Activation rate for EDC.
- `k1_2`: Activation rate for DIC.
- `K1`: Ratio of O-acylurea to anhydride vs. direct hydrolysis for EDC.
- `K2`: Ratio of O-acylurea to anhydride vs. direct hydrolysis for DIC.
- `k2`: Conversion rate of anhydride back to acid.
- `k0_1`: Background reaction rate for EDC.
- `k0_2`: Background reaction rate for DIC.
- `Ac`: Acid concentration.
- `F1`: EDC concentration (Fuel 1).
- `F2`: DIC concentration (Fuel 2).
- `W1`: Urea concentration from EDC.
- `W2`: Urea concentration from DIC.
- `An`: Anhydride concentration.

### Notes

- `F1` and `F2` represent EDC and DIC, respectively.
- `W1` and `W2` are the corresponding ureas produced from EDC and DIC.

## Example Simulation

To simulate the model under specific conditions, modify the `kinmodel.py` file to set the desired initial concentrations and rate constants. Then, run the script to generate the simulation results.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
