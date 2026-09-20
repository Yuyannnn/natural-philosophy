#!/usr/bin/env python3
"""Check x'' + damping*x' + x = 0 in nondimensional variables.

One unit mass and spring constant; RK4 is used for an educational comparison.
This verifies the ODE implementation, not any real material or device.
"""
from math import cos, sin, hypot


def trajectory(step, damping=0.0, duration=20.0):
    count = round(duration / step)
    assert abs(count * step - duration) < 1e-12
    x, v = 1.0, 0.0
    yield 0.0, x, v

    def rhs(position, velocity):
        return velocity, -position - damping * velocity

    for index in range(count):
        a, b = rhs(x, v)
        c, d = rhs(x + step*a/2, v + step*b/2)
        e, f = rhs(x + step*c/2, v + step*d/2)
        g, h = rhs(x + step*e, v + step*f)
        x += step * (a + 2*c + 2*e + g) / 6
        v += step * (b + 2*d + 2*f + h) / 6
        yield (index + 1) * step, x, v


def main():
    errors = []
    for step in (0.1, 0.05):
        samples = list(trajectory(step))
        error = max(hypot(x - cos(t), v + sin(t)) for t, x, v in samples)
        drift = max(abs((x*x + v*v)/2 - 0.5) for _, x, v in samples)
        errors.append(error)
        print(f"dt={step:.2f}: max state error={error:.3e}, energy drift={drift:.3e}")
    assert errors[0] / errors[1] > 12, "Expected fourth-order convergence"
    assert errors[1] < 2e-6

    damping = 0.2
    damped = list(trajectory(0.05, damping))
    energies = [(x*x + v*v)/2 for _, x, v in damped]
    assert all(after <= before + 1e-12 for before, after in zip(energies, energies[1:]))
    # Independent energy balance: integrate dissipation c*v^2 with trapezoids.
    loss = sum(
        damping * (v0*v0 + v1*v1) * (t1-t0)/2
        for (t0, _, v0), (t1, _, v1) in zip(damped, damped[1:])
    )
    balance_error = abs(energies[-1] - energies[0] + loss)
    assert balance_error < 1e-5
    print(f"Damped energy balance error={balance_error:.3e}")
    print("PASS: analytic solution, step refinement, and energy balance.")


if __name__ == "__main__":
    main()
