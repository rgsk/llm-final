### How much weight decay shrinks the weights?

explaination of `test_decay_alone_shrinks_a_weight_by_24_percent_over_mains_run` in `tests/test_train.pyn`

**1. Each step multiplies.** With xₜ = lrₜ · weight_decay for step t:

```
w_end = w_start · (1 − x₀)(1 − x₁) … (1 − x₄₉₉₉)
```

**2. A logarithm turns the product into a sum:**

```
ln(w_end / w_start) = ln(1 − x₀) + ln(1 − x₁) + … + ln(1 − x₄₉₉₉)
```

**3. For a small x, ln(1 − x) ≈ −x.** The full series is ln(1 − x) = −x − x²/2 − x³/3 − …. Here x is at most 1e-3 · 0.1 = 1e-4, so x² is at most 1e-8, and every term after the first is negligible:

```
ln(w_end / w_start) ≈ −(x₀ + x₁ + … + x₄₉₉₉) = −weight_decay · (lr₀ + lr₁ + … + lr₄₉₉₉)
```

**4. Undo the logarithm:**

```
w_end / w_start ≈ e^(−weight_decay · sum of lrs)
```

**5. The sum is steps × the average lr:** 5000 × 5.5e-4 ≈ 2.75. So the exponent is 0.1 × 2.75 = 0.275, and e^(−0.275) ≈ 0.76.

**Why it's worth knowing.** The total decay depends only on weight_decay × the sum of lrs, not on how the lr is spread across the run. So if you double `max_steps` with the same lr range, the sum doubles, and a weight that no gradient supports shrinks to e^(−0.55) ≈ 0.58 instead of 0.76. That's one reason weight decay matters more in longer runs.
