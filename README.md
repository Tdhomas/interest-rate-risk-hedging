# Interest Rate Risk Management of a Fixed Income Portfolio
A complete fixed-income hedging framework combining duration/convexity analysis, SOFR and Treasury futures, the Vasicek interest-rate model, and Monte Carlo simulation.

## Overview

This project replicates a real sell-side risk management workflow. We construct a $100M US Treasury bond portfolio, analyze its interest-rate sensitivities, hedge its duration and convexity exposure with financial futures, and evaluate hedge effectiveness under a stochastic short-rate model.

All methodology aligns with the project instruction from N. Gershun (see docs/assignment.pdf).

---

## Objectives

1. Retrieve and process US Treasury and SOFR market data  
2. Build a diversified fixed-income portfolio and compute:
   • Cash flows  
   • Accrued interest and invoice price  
   • Modified duration and convexity  
3. Derive durations and convexities of futures underlyings using:
   • Cheapest-to-deliver (CTD) for Treasury futures  
   • Short-rate exposure approximation for SOFR futures  
4. Hedge the portfolio duration:
   • From 5 years to 1 year using SOFR futures  
   • From 5 years to 1 year using Treasury futures  
5. Hedge both duration and convexity simultaneously  
6. Estimate Vasicek model parameters using Maximum Likelihood  
7. Simulate 100,000 Monte Carlo short-rate paths  
8. Compare hedge performance using:
   • Mean returns  
   • Standard deviations  
   • 95% VaR and Expected Shortfall  

---

## Data & Instruments

• Ten US Treasury coupon bonds of different maturities  
• One 3-Month SOFR futures contract (SR3)  
• One US Treasury futures contract (T-Note or T-Bond), with CTD selection  

Data sources:
• Bloomberg Terminal (bond quotes and futures CTD information)  
• NY Federal Reserve (Daily Simple SOFR, ~500 observations)  

---

## Methodology Summary

### Bond Analytics

For a representative example bond:
• Price conversion from ticks to dollars  
• Semi-annual coupon cash flow timeline  
• Accrued interest + invoice price  
• Duration and convexity:
  - Equation-based derivation  
  - Bloomberg verification and discrepancy commentary  

We generalize the analytics to all 10 portfolio bonds.

### Portfolio Construction

Target:
> Modified duration = 5 years, Total market value = $100M

• Optimization selects weights subject to duration and size constraints  
• Rationale documented (liquidity, maturity laddering, yield considerations)

### Hedging Strategies

1. **Duration Hedge with SOFR Futures**
   - Selection of appropriate expiry  
   - Calculation of hedge ratio and contract count  

2. **Duration Hedge with Treasury Futures**
   - Identification of CTD  
   - Use of conversion factor and DV01 relationship  

3. **Duration + Convexity Hedge**
   - Joint optimization: target duration = 1, convexity = 0  

### Vasicek Calibration

Short rate process:
> dr = α(μ − r) dt + σ dW

MLE applied to SOFR daily time series with dt = 1/360  
(see docs/vasicek_note.pdf for formal derivation)

Estimated parameters:
• Mean reversion speed α  
• Long-run mean μ  
• Volatility σ  

### Monte Carlo Simulation

• 100,000 mean-reverting interest-rate paths over 3 months  
• Parallel yield curve shift assumption  
• Portfolio and hedge valuations computed along each path  

Performance metrics reported:
• Mean  
• Standard deviation  
• VaR 95%  
• Expected Shortfall 95%  
