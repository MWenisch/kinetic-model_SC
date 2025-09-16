import textwrap
from kinmodel import KineticModel


def equations(concs, t, *ks):
    Ac, F1, F2, W1, W2, An = concs
    k1_1, k1_2, K1, K2, k2, k0_1, k0_2 = ks

    return [- k1_1*F1*Ac + k2*An + (k1_1*K1*Ac*F1)/(K1+1),(k1_2*K2*Ac*F2)/(K2+1)
            - k1_1*F1*Ac -k0_1*F1,
            - k1_2*F2*Ac -k0_2*F2,
            + k1_1*F1*Ac +k0_1*F1,
            + k1_2*F2*Ac +k0_2*F2,
            + (k1_1*Ac*F1)/(K1+1)+(k1_2*Ac*F2)/(K2+1) - k2*An]


model = KineticModel(
    name="Boek_2fuels",
    description=textwrap.dedent("""\
        Diacid kinetics w/o catalysis; two competing fuels:

                Ac + F1 ---> I1       (k1_1)
                Ac + F2 ----> I2      (k1_2)
                I1 ---> An + W1  (kiAn_1)
                I1 ---> Ac + W1  (kiAc_1)
                I2 ---> An + W2  (kiAn_2)
                I2 ---> Ac + W2  (kiAc_2)
                An ---> Ac      (k2)

        Steady-state approximation with K_i = kiAc_i/kiAn_i with i=1,2.
        Orders: k1_1,k1_2, K1, K2, k2, k0_1, k0_2; Ac, F1, F2, W1, W2, An.\
        """),
    kin_sys=equations,
    ks_guesses=[0.02, 0.01, 0.01, 0.01, 1.2],
    ks_constant=[1.8e-4, 2.9e-4],
    conc0_guesses=[5, 5, 20],
    conc0_constant=[0, 0, 0],
    k_var_names=["k1_1","k1_2","K1","K2","k2"],
    k_const_names=["k0_1","k0_2"],
    conc0_var_names=["[Acid]0","[EDC]0","[DIC]0"],
    conc0_const_names=["[W1]0", "[W2]0","[An]0"],
    legend_names=["Acid", "EDC", "DIC", "Urea1", "Urea2","An"],
    top_plot=[1, 2],
    bottom_plot=[0, 3],
    sort_order=[1, 3, 2, 0],
    int_eqn=[
            lambda cs, ks: ks[2]*cs[3], ],
    int_eqn_desc=[
            "k2*An", ],
    lifetime_conc=[3],
    rectime_conc=[0],
    )
model.simulate()
