---
title: San Bernardino International Airport
description: How SBD moved from reactive airfield operations to AI-driven predictive maintenance with LAIRA and ArcGIS. Featured by Esri.
---

# San Bernardino International Airport

How SBD moved from reactive airfield operations to AI-driven predictive maintenance with LAIRA and ArcGIS — a continuous-scan capture and inspection workflow running on the airport's own operations vehicles.

[Read the full SBD case study at esri.com ↗](https://www.esri.com/en-us/lg/industry/transportation/stories/san-bernardino-international-airport-arcgis-airfield-operations)

---

## At a glance

| Metric | Value | Source |
|:---|:---|:---|
| Surface anomalies detected vs. manual | 3–7× | Esri case study |
| Data points captured per LAIRA pass | 2M+ | Continuous scan, 55 mph |
| Field validation time reduction | 50%+ | Esri case study |
| Compliance baseline | FAA Part 139 | Established |

---

## The problem — manual airfield inspection tops out at 20–40 observations per shift

Before LAIRA, SBD's airfield inspection workflow looked like every other Part 139 airport's: certified inspectors driving the airfield by hand, recording observations on paper logs, transcribing to spreadsheets at end of shift. Coverage was inconsistent across shifts and weather; early-stage defects routinely went undetected; data was fragmented across formats that didn't roll up into a maintenance plan.

The constraint wasn't the inspectors. The constraint was the medium: a single human observer captures 20–40 observations per shift. The airfield generates orders of magnitude more data than that.

> Manual inspections produced only 20–40 observations per shift with inconsistent results, leaving defects undetected and fragmented across logs.
>
> — Esri case study

---

## The solution — LAIRA captures continuously, ArcGIS makes it actionable

SBD partnered with Airwai to deploy LAIRA — the Layered Autonomous Inference and Reasoning Agent platform — integrated directly into the airport's existing Esri ArcGIS stack. The rig mounts on operations vehicles already in service; capture happens passively as the vehicle drives. Every pass writes ~2 million data points to the cloud, runs them through edge-AI inference, and publishes geo-tagged anomalies straight into the airport's ArcGIS Online environment. ArcGIS Field Maps directs maintenance crews to prioritized repair locations. ArcGIS Dashboards give airport leadership real-time operational oversight across the entire airfield.

### Detection categories

**01 · Pavement defects.** Cracks, raveling, weathering, depressions, faulting — classified, geo-tagged, severity-scored.

**02 · Foreign object debris.** FOD detection on runway and taxiway, classified by material and risk.

**03 · Vegetation encroachment.** Edge-of-pavement intrusion, AOA boundary monitoring, perimeter integrity.

**04 · Marking degradation.** Runway, taxiway, and apron marking wear, retroreflectivity screening, MUTCD-grade classification.

---

## Leadership quotes

> By deploying AI-driven airfield intelligence within our GIS environment, airports can move from reactive operations to predictive, data-led management.
>
> — Mike Burrows · CEO · San Bernardino International Airport

> Our team has a consistent, objective baseline across shifts and conditions, strengthening our compliance posture without adding burden to staff.
>
> — Jonathan Galvan · Manager · San Bernardino International Airport

---

## The outcome — from reactive to predictive

The shift wasn't a one-time upgrade. It was a workflow inversion. Continuous-scan capture produced a baseline so dense that maintenance planning could move from *respond when something fails* to *schedule before something fails*. Field validation, the most labor-intensive step in any inspection workflow, dropped by more than 50% because crews no longer hunt for issues — they confirm flagged ones.

The airfield now has a persistent digital twin: every linear foot of pavement, every marking, every vegetation boundary represented as live geospatial data in the airport's own ArcGIS environment. As LAIRA continues to capture, the twin compounds.

**3–7× more surface anomalies detected. 2M+ data points per pass. 50%+ faster field validation. FAA Part 139 compliance posture documented continuously rather than annually.**

---

## What's running at SBD today

Operational, continuous, and integrated into the team's existing workflow.

| Aspect | Detail |
|:---|:---|
| Capture cadence | Weekly operator drives · airfield surfaces + groundside corridors |
| Sensor platform | LAIRA Rig · 128-channel LiDAR · 4K RGB · RTK GNSS · 6-axis IMU + VIO · NVIDIA edge inference |
| Detection categories | Pavement distress · FOD · vegetation encroachment · marking degradation |
| Output destination | ArcGIS Online feature service · Field Maps · Dashboards |
| Standards mapping | FAA AC 150/5320-17 · ASTM D5340 PCI · MUTCD Part 3 markings |
| Deployment role | Beta operating partner · since 2025 |

---

## Schedule a 30-day pilot on your airfield

A pilot is one corridor, your operations vehicle, and your existing ArcGIS endpoint. Output is an audit-ready section report against ASTM D5340 + FAA AC 150/5320-17, delivered in 30 days.

[Schedule a pilot →](../pricing.md#scope){ .md-button .md-button--primary }
[Read Esri's case study ↗](https://www.esri.com/en-us/lg/industry/transportation/stories/san-bernardino-international-airport-arcgis-airfield-operations){ .md-button }
