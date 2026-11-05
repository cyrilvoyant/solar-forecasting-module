# Forecasting the intermittent solar resource: a 10-hour learning module

Draft 2026-11-05. Learning path for the JOSE submission. Nothing is published yet.

This module teaches how to forecast hourly solar radiation one hour ahead, from the position of the Sun to the evaluation of a model. It follows the course given at Mines Paris - PSL (UE14, first year of the civil engineering curriculum), at the University of Corsica and in a ParisTech school (second year).

Everything runs in a browser or in MATLAB/Python. The interactive pages and the codes already exist; this repository puts them in order, says what to do with each one and why.

## Who it is for

- engineering and master students (energy, environment, applied mathematics);
- instructors who want a ready-to-use sequence on solar forecasting;
- engineers who need to judge a forecast before buying or building one.

Prerequisites: basic statistics (mean, variance, correlation), linear algebra (matrix product), and a little MATLAB or Python.

## Learning objectives

At the end, you will be able to:

1. explain why the grid needs solar forecasts, and in which unit (irradiance, irradiation, PV power);
2. describe the components of the global horizontal irradiance (GHI) and its double seasonality (day, year);
3. remove the solar cycle with a clear-sky model and the clear-sky index (CSI);
4. measure how variable and how forecastable a site is (sCV, F);
5. build an AR(p) model as a linear regression and estimate it by least squares;
6. compare any model with simple references (persistence, smart persistence) using nRMSE, nMBE, skill score and NICE;
7. train an Extreme Learning Machine (ELM) and an online (sliding-window) model, and decide when complexity is worth it (frugality).

## Notations (valid for the whole module)

| Symbol | Meaning |
|---|---|
| GHI_t | global horizontal irradiation measured at hour t (Wh/m²) |
| GHI_cs,t | clear-sky GHI (Solis model) |
| CSI_t | clear-sky index: GHI_t − GHI_cs,t (Wh/m²) |
| y_t | centred CSI: CSI_t − μ |
| h | horizon, in time steps (here Δt = 1 h) |
| p | number of lags of the AR model |
| L | number of hidden neurons of the ELM |

## The data

Hourly GHI measured at Ajaccio (Corsica, 41.9° N, 8.8° E, 4 m), Météo-France, 1998–2007. Training 1998–2005, validation 2006, test 2007.

> TODO (Cyril): the Météo-France file cannot be redistributed here without checking its licence. Options: point to the data source, or use an open dataset for the exercises.

## The sequence: 5 sessions of 2 hours, plus group work at home

Each session: a short lecture (slides of the course), then the interactive pages, then the code. The questions at the end of each session check understanding; they are not graded.

### Before session 1 (home, individual): literature review

Read and summarise the vocabulary and phenomena: solar radiation and its measurement, why and how we forecast, time series and the clear-sky model, least squares and ELM. Deliverable: 4 to 5 pages with figures.

### Session 1 · Why forecast solar? Solar radiation

- Why forecast: the grid must anticipate PV production; irradiance (W/m²) vs irradiation (Wh/m²).
- Direct, diffuse and global radiation; attenuation by the atmosphere; position of the Sun (zenith angle, declination).
- The double seasonality of the GHI.

Interactive: The Sun, the seasons and UTC ([EN](https://www.cyrilvoyant.com/tools/sun-seasons-utc/) · [FR](https://www.cyrilvoyant.com/fr/animations/soleil-saisons-utc/)). Move the date and the hour; watch the zenith angle and the day length.

Read: [Solar forecasting basics, §1](https://cyrilvoyant.github.io/teaching/solar-forecasting-basics.html).

Questions:
- Why is the GHI zero at night and maximal near solar noon?
- Why must solar data be time-stamped in UTC (or solar time) and not in local time?

### Session 2 · Time series, clear sky and clear-sky index

- A time series: trend, seasonality, cycles, residual; additive or multiplicative.
- Horizon and time step; a predictable part plus an error.
- The clear-sky model (Solis, Beer-Lambert idea); the CSI as a difference; is the CSI stationary?

Read: [Solar forecasting basics, §2](https://cyrilvoyant.github.io/teaching/solar-forecasting-basics.html); [Forecasting the solar resource made simple](https://cyrilvoyant.github.io/methods/solar-forecasting-made-simple.html) ([FR](https://www.cyrilvoyant.com/prevision-solaire-faire-simple/)).

Code: [Make_Stationary](https://github.com/cyrilvoyant/Make_Stationary): remove the seasonality of hourly GHI, then compare the monthly mean and standard deviation of GHI and CSI.

Questions:
- Why a difference (additive model) rather than a ratio (GHI / GHI_cs) near sunrise and sunset?
- The monthly mean of GHI goes from 163 to 521 Wh/m²; what happens to the CSI?

### Session 3 · Variability, forecastability, and the AR model

- A variable site is not necessarily unforecastable: sCV (variability) and F (forecastability, which depends on the horizon).
- AR(1) with numbers, then AR(p) written as a linear regression y = Xw + ε.
- Least squares: normal equations and geometric interpretation (projection).
- Training, validation, test; choosing p with ACF/PACF (filter) or with the validation error (wrapper).

Interactive:
- Measure variability and forecastability, sCV and F ([EN](https://cyrilvoyant.github.io/methods/solar-variability-scv.html#try-it) · [FR](https://www.cyrilvoyant.com/fr/outils/variabilite-previsibilite/#try-it)).
- Which forecast for which signal? ([EN](https://www.cyrilvoyant.com/stories/variability-memory-forecastability/#experience) · [FR](https://www.cyrilvoyant.com/fr/recits/variabilite-memoire-previsibilite/#experience)).

Read: [Solar forecasting basics, §3 to §5](https://cyrilvoyant.github.io/teaching/solar-forecasting-basics.html).

Code: [solar-variability-scv](https://github.com/cyrilvoyant/solar-variability-scv).

Questions:
- Build X and y by hand for five CSI values and p = 2.
- ACF(1) = 0.84 on Ajaccio: what does it say about the next hour?

### Between sessions 3 and 4 (home, groups): model your own series

Each student picks a different time series on the Internet and forecasts it one step ahead with 5 methods: persistence, AR, ELM, AR on the differenced series, ELM on the differenced series. Each reports 4 descriptive statistics and 5 error metrics in common tables. The group shares one public GitHub repository, with reusable functions (metrics, models) that will serve the final project.

### Session 4 · Evaluate: always compare with a reference

- References: simple persistence, smart persistence (clear-sky persistence), BLEND, ARTU.
- Errors: nMBE, MAE, RMSE, nRMSE; day only or day + night?
- Skill score and NICE: does the model beat persistence?
- Bias: effect of the night rule and of the "no negative forecast" rule.

Interactive:
- Compare a forecast with persistence, NICE ([EN](https://cyrilvoyant.github.io/methods/nice-metrics.html#try-it) · [FR](https://www.cyrilvoyant.com/fr/outils/nice/#try-it)).
- Compute BLEND weights ([EN](https://cyrilvoyant.github.io/methods/persistence-blend.html#try-it) · [FR](https://www.cyrilvoyant.com/fr/outils/blend/#try-it)).
- Explore ARTU coefficients ([EN](https://cyrilvoyant.github.io/teaching/artu-worked-example.html#try-it) · [FR](https://www.cyrilvoyant.com/fr/outils/artu/#try-it)).
- Displace a forecast and explore the γ-index ([EN](https://cyrilvoyant.github.io/methods/gamma-index.html#try-it) · [FR](https://www.cyrilvoyant.com/fr/outils/indice-gamma/#try-it)).

Read: [Evaluate a solar forecast against persistence](https://www.cyrilvoyant.com/stories/evaluate-solar-forecast-persistence/) ([FR](https://www.cyrilvoyant.com/fr/recits/evaluer-prevision-solaire-persistance/)); [Solar forecasting basics, §6](https://cyrilvoyant.github.io/teaching/solar-forecasting-basics.html).

Code: [nice-metrics](https://github.com/cyrilvoyant/nice-metrics), [ARTU](https://github.com/cyrilvoyant/ARTU).

Questions:
- Why does the nRMSE of the AR go from 21 % (day only) to 30 % (day + night), while its RMSE drops from 79 to 56 Wh/m²?
- A model has SS < 0: what do you tell the client?

### Session 5 · ELM, online learning, frugality

- ELM: one hidden layer, random input weights, output weights by least squares; choosing L; the result depends on the draw.
- Calendar inputs: sin/cos encoding of the hour and the day; stationarise or give the hour?
- Online learning: sliding window, which length?
- Frugality: good accuracy with little computing, data and maintenance.

Interactive: Compare forecasts, persistence, AR and ELM against horizon ([EN](https://www.cyrilvoyant.com/tools/forecast-comparison/) · [FR](https://www.cyrilvoyant.com/fr/outils/comparateur-previsions/)).

Read: [Solar forecasting basics, §7 and §8](https://cyrilvoyant.github.io/teaching/solar-forecasting-basics.html); [Frugal solar forecasting](https://cyrilvoyant.github.io/methods/frugal-solar-forecasting-en.html) ([FR](https://www.cyrilvoyant.com/prevision-solaire-modeles-frugaux/)); [A deep-learning model against a simple baseline](https://www.cyrilvoyant.com/stories/solar-forecast-baseline-deep-learning/) ([FR](https://www.cyrilvoyant.com/fr/recits/reference-prevision-solaire-deep-learning/)).

Code: [PV_ELM_pred](https://github.com/cyrilvoyant/PV_ELM_pred).

Questions:
- Why do 20 draws of the ELM give 20 different models, and what do you keep?
- Is an ELM worth it if it gains 1 % of nRMSE over the AR?

### After session 5 (home, groups): final project, a role play

The group is an engineering firm consulted by the developer of a smart district (rooftop PV, batteries, charging stations). The energy management system needs a one-hour-ahead GHI forecast. The firm recommends: build the forecast in-house, buy it from a provider, or subscribe to a numerical weather prediction service. If in-house: which model, which accuracy, how to run and maintain it, at what cost. Deliverables: a professional report and the group's GitHub repository.

## For instructors

- Duration: 10 hours in class (5 × 2 h) plus group work at home.
- First year: sessions 1 to 4 and the AR only. Second year: the full module with ELM and online learning.
- Software: MATLAB advised, Python possible.
- The slides of the course: TODO (Cyril: publish the PDF of the lecture here, under CC BY?).

## Repository layout

The pages and codes are not copied here. They are pinned submodules, fixed at the version used by the module, so every number stays reproducible.

| Folder | Content | Licence |
|---|---|---|
| `materials/www` | source of www.cyrilvoyant.com: interactive pages (`tools/`, `fr/animations/`, `fr/outils/`) and stories (`stories/`, `fr/recits/`) | CC BY 4.0 (stated on each page) |
| `materials/cyrilvoyant.github.io` | worked examples (`teaching/`) and method pages (`methods/`) | CC BY 4.0 (stated on each page) |
| `materials/Make_Stationary` | remove the seasonality of hourly GHI (MATLAB) | see its LICENSE |
| `materials/solar-variability-scv` | sCV and forecastability (MATLAB) | see its LICENSE |
| `materials/nice-metrics` | NICE metrics | see its LICENSE |
| `materials/ARTU` | ARTU reference model | see its LICENSE |
| `materials/PV_ELM_pred` | persistence, AR and ELM benchmark | see its LICENSE |

Clone with the submodules:

```
git clone --recurse-submodules https://github.com/cyrilvoyant/solar-forecasting-module.git
```

## How to cite

TODO after acceptance (JOSE DOI and Zenodo archive).

## Licence

Text and figures: CC BY 4.0. Code: MIT. See LICENSE.

## Contributing

Questions, errors, suggestions: open an issue. See CONTRIBUTING.md.
