---
title: 'Forecasting the intermittent solar resource: a 10-hour computational learning module, from the position of the Sun to the cost of a model'
tags:
  - solar energy
  - solar radiation forecasting
  - time series
  - persistence
  - autoregressive model
  - extreme learning machine
  - engineering education
authors:
  - name: Cyril Voyant
    orcid: 0000-0003-0242-7377
    affiliation: 1
affiliations:
  - name: Mines Paris - PSL, O.I.E. center (Observation, Impacts, Energy), Sophia Antipolis, France
    index: 1
date: 5 November 2026
bibliography: paper.bib
---

# Summary

Solar production follows the clouds. To integrate it into the grid, to drive a battery or to sell electricity at the right price, it must be forecast, here one hour ahead. This module teaches how to do it, step by step, on ten years of hourly global horizontal irradiation (GHI) measured at Ajaccio, Corsica.

The module lasts 10 hours in class (five sessions of 2 hours) plus group work at home. It follows one chain that comes back in every session: GHI measurements, clear-sky model, clear-sky index (CSI), centring, chronological split, model (persistence, AR, ELM), forecast, back to GHI, evaluation. Each session combines a short lecture, interactive browser pages and open MATLAB/Python codes. All pages exist in English and French.

# Statement of need

Students and engineers who start in solar forecasting find two kinds of material: research papers, which assume the basics, and generic machine-learning tutorials, which skip them. Neither says what to do first: remove the solar cycle, measure how forecastable the site is, and compare any model with a simple reference.

This last point is the core of the module. A model that does not beat persistence brings nothing. On the Ajaccio test year (2007), the smart persistence divides the RMSE of the simple persistence by 1.7; the AR(2) gains 3 % over it, and the ELM 7 %. The good question is therefore not "what is the best model?" but "is the gain worth the cost?" (computing, data, maintenance, monitoring). This frugal view is rarely taught, although it is what an engineer needs to decide whether to build a forecast, buy it, or subscribe to a weather service.

The module is built on published, open research tools: benchmarks for solar forecasting [@voyant2022benchmarks], the clear-sky index and its role in short-term forecasting [@voyant2025clearsky], the stochastic coefficient of variation and forecastability [@voyant2026scv], and the NICE metrics [@voyant2025nice]. It gives students a guided entry into this literature [@voyant2017review].

# Learning objectives

At the end, students can:

- explain why the grid needs solar forecasts, and in which unit;
- describe the components of the GHI and its double seasonality (day, year);
- remove the solar cycle with a clear-sky model [@ineichen2008solis] and the CSI;
- measure the variability and the forecastability of a site;
- build an AR(p) model as a linear regression and estimate it by least squares [@box2015time; @hyndman2021fpp3];
- compare any model with persistence (nRMSE, nMBE, skill score, NICE);
- train an Extreme Learning Machine [@huang2006elm] and an online model, and judge their frugality.

# Content and instructional design

| Session | Topic | Interactive pages and codes |
|---|---|---|
| 1 | Why forecast solar? Solar radiation, position of the Sun | Sun, seasons and UTC |
| 2 | Time series, clear sky, CSI, stationarity | Make_Stationary |
| 3 | Variability (sCV), forecastability (F), AR(p), least squares | sCV and F explorer; which forecast for which signal? |
| 4 | References and evaluation: persistence, BLEND, ARTU, NICE | NICE, BLEND, ARTU, γ-index explorers |
| 5 | ELM, online learning, frugality | persistence/AR/ELM comparator; PV_ELM_pred |

The design follows three choices.

1. **One chain, always the same.** The nine steps of the forecasting chain are shown at the start and highlighted in each chapter. Students always know where they are.
2. **Numbers before abstraction.** Each concept is first computed by hand on a few values (AR(1) with numbers, the matrix X built from five CSI values), then generalised.
3. **Learn by doing, at home and in groups.** Three pieces of work frame the sessions: a literature review before session 1; between sessions 3 and 4, each student forecasts a time series of their choice with five methods and the group shares one GitHub repository of reusable functions; after session 5, a role play where the group, as an engineering firm, advises the developer of a smart district: build the forecast in-house, buy it, or subscribe to a numerical weather prediction service.

The interactive pages let students change one parameter at a time (date, horizon, number of lags, window length) and see the effect immediately. The codes reproduce every number of the lecture.

# Experience of use

TODO (Cyril, in your own words): how the course came to be; where and since when it is taught (Mines Paris - PSL, UE14, first year; University of Corsica; ParisTech school, second year); number of students; what worked, what you changed (e.g. the clear-sky index as a difference rather than a ratio, day-only vs day + night errors); what students produce in the final role play.

# Acknowledgements

TODO (Cyril): colleagues, data provider (Météo-France), funding if any.

# References
