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

Solar production follows the clouds. To put it on the grid, to drive a battery or to sell electricity at the right time, it must be forecast; here, one hour ahead. This module teaches how, on eleven years of hourly global horizontal irradiation (GHI) measured at Ajaccio, Corsica (Météo-France open data).

It lasts 10 hours in class (five sessions of 2 hours), plus group work at home. One chain comes back in every session: GHI, clear-sky model, clear-sky index (CSI), centring, chronological split, model (persistence, AR, ELM), forecast, back to GHI, evaluation. Each session mixes a short lecture, interactive pages that run in the browser, and open MATLAB codes. The pages exist in English and French.

# Statement of need

A student who starts in solar forecasting finds research papers, which assume the basics, and machine-learning tutorials, which skip them. Neither says what to do first: remove the solar cycle, measure how forecastable the site is, and compare any model with a simple reference.

This is the core of the module. A model that does not beat persistence brings nothing. On the Ajaccio test year (2007), the smart persistence divides the RMSE of the simple persistence by 1.7; the AR(2) gains 3 % over it, the ELM 7 %. So the question is not "which model is the best?" but "is the gain worth the cost?": computing, data, maintenance, monitoring. An engineer needs this to decide whether to build a forecast, buy it, or subscribe to a weather service. It is rarely taught.

The module rests on published, open tools: benchmarks for solar forecasting [@voyant2022benchmarks], the role of the clear-sky model [@voyant2025clearsky], the stochastic coefficient of variation and forecastability [@voyant2026scv], the NICE metrics [@voyant2025nice]. It is also a guided entry into the literature [@voyant2017review].

# Learning objectives

At the end, students can:

- say why the grid needs solar forecasts, and in which unit;
- describe the components of the GHI and its double seasonality (day, year);
- remove the solar cycle with a clear-sky model [@ineichen2008solis] and the CSI;
- measure the variability and the forecastability of a site;
- write an AR(p) model as a linear regression and estimate it by least squares [@box2015time; @hyndman2021fpp3];
- compare any model with persistence (nRMSE, nMBE, skill score, NICE);
- train an Extreme Learning Machine [@huang2006elm] and an online model, and judge whether they are worth it.

# Content and instructional design

| Session | Topic | Pages and codes |
|---|---|---|
| 1 | Why forecast solar? Radiation, position of the Sun | Sun, seasons and UTC |
| 2 | Time series, clear sky, CSI, stationarity | Make_Stationary |
| 3 | Variability (sCV), forecastability (F), AR(p), least squares | sCV and F; which forecast for which signal? |
| 4 | References and evaluation: persistence, BLEND, ARTU, NICE | NICE, BLEND, ARTU, γ-index |
| 5 | ELM, online learning, frugality | persistence/AR/ELM comparator; PV_ELM_pred |

Three choices.

1. **One chain, always the same.** The nine steps are shown at the start and highlighted in each chapter. Students know where they are.
2. **Numbers before formulas.** Each idea is first computed by hand on a few values (an AR(1) with numbers, the matrix X built from five CSI values), then written in general.
3. **Do it, in groups, at home.** A literature review before session 1. Between sessions 3 and 4, each student forecasts a time series of their choice with five methods, and the group shares one GitHub repository of reusable functions. After session 5, a role play: the group is an engineering firm that advises the developer of a smart district. Build the forecast, buy it, or subscribe to a numerical weather prediction service?

The pages change one parameter at a time (date, horizon, number of lags, window length) and show the effect at once. The codes reproduce the large majority of the numbers of the lecture.

# Experience of use

The course has been taught for ten years, to about ten students each time: at the University of Corsica, in the Paoli Tech engineering school (second and third year), and at Mines Paris - PSL, in UE14, as a mini-project on forecasting and energy systems. The material changed over the years; the interactive pages and the open codes are the latest addition.

# Availability

Repository, learning path and licences: <https://github.com/cyrilvoyant/solar-forecasting-module> (text CC BY 4.0, code MIT), archived on Zenodo [doi:10.5281/zenodo.23987900](https://doi.org/10.5281/zenodo.23987900). The pages and codes are pinned submodules, archived by Software Heritage. Data: Météo-France open data, Licence Ouverte 2.0, with a script that rebuilds the file.

# Acknowledgements

The author thanks the students of Paoli Tech and Mines Paris - PSL, whose questions shaped this material, and Météo-France for the open data.

# References
