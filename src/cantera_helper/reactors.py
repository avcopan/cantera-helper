"""Cantera reactors."""

from collections.abc import Mapping

import cantera as ct
from cantera import ReactorNet, Solution  # pyright: ignore[reportAttributeAccessIssue]


def jsr(
    model: Solution,
    T: float,
    P: float,
    residence_time: float,
    volume: float,
    concentrations: Mapping[str, float],
) -> ReactorNet:
    """Run a jet-stirred reactor simulation.

    :param model: Chemical kinetics model
    :param T: Temperature
    :param P: Pressure
    :param residence_time: Residence time
    :param concentrations: Starting concentrations
    :return: Solved simulation reactor network
    """
    # Use concentrations from the previous iteration to speed up convergence
    model.TPX = T, P * ct.one_atm, concentrations  # pyright: ignore[reportAttributeAccessIssue]

    # Set up JSR: inlet -> flow control -> reactor -> pressure control -> exhaust
    volume_m3 = volume * (1e-2) ** 3
    reactor = ct.IdealGasReactor(model, energy="off", volume=volume_m3)  # pyright: ignore[reportAttributeAccessIssue]
    exhaust = ct.Reservoir(model)  # pyright: ignore[reportAttributeAccessIssue]
    inlet = ct.Reservoir(model)  # pyright: ignore[reportAttributeAccessIssue]
    ct.PressureController(  # pyright: ignore[reportAttributeAccessIssue]
        upstream=reactor,
        downstream=exhaust,
        K=1e-3,
        primary=ct.MassFlowController(  # pyright: ignore[reportAttributeAccessIssue]
            upstream=inlet,
            downstream=reactor,
            mdot=reactor.mass / residence_time,
        ),
    )
    reactor_net = ct.ReactorNet([reactor])  # pyright: ignore[reportAttributeAccessIssue]
    reactor_net.advance_to_steady_state(max_steps=100000)
    return reactor
