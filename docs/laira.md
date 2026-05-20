# Three procurements collapse to one.

If your team is running manual airfield inspections, contracting per-mile pavement data, or commissioning sidewalk and ADA surveys separately — LAIRA replaces all three with one continuous capture and audit-ready output published directly to your ArcGIS environment.

[Schedule a pilot →](pricing.md#scope){ .md-button .md-button--primary }
[See the technical data sheet](#datasheet){ .md-button }

---

## At a glance

| Metric | Value |
|:---|:---|
| Observations per shift via manual inspection | 20–40 |
| Data points captured per LAIRA pass | 2M+ |
| Compliance standards in one workflow | 7 (ASTM · AASHTO · FAA · UFC · PROWAG · MUTCD · 23 CFR) |
| Field validation time reduction | 50%+ |

---

## You're running three procurements that should be one

### 01 · Manual inspection

Your people spend hours capturing what software can capture continuously. Certified inspectors driving the airfield, recording observations on paper logs, transcribing to spreadsheets at end of shift. 20–40 observations per shift is the ceiling. Coverage is inconsistent across shifts, weather, and personnel. Early-stage defects routinely go undetected. **Cost:** inspector time you don't have, against a backlog that compounds.

### 02 · Per-mile pavement data

Recurring contracts for data you should own. An ARAN-class vendor runs a truck across your network and bills you per lane-mile. Every cycle. The data lands in their portal, in their format, on their timeline. Your engineers can't easily query it. **Cost:** $95+/lane-mile recurring, plus mobilization, plus reformat labor.

### 03 · Separate sidewalk + ADA

PROWAG geometry is a third procurement, with a different vendor. Sidewalk cross-slope, running slope, curb-ramp flare, vertical discontinuity at panel joints — all measured by a separate accessibility subcontract. Comes back weeks after the pavement data, in a different format. **Cost:** separate procurement vehicle, separate budget line, separate annual cycle.

**LAIRA collapses all three into one continuous-scan capture, run from a vehicle your team already operates, with outputs published natively to the ArcGIS environment your engineers already use.** No new vendor portal. No reformatting. No second mobilization.

---

## Three ways to feed it

LAIRA is software. We use commercial off-the-shelf hardware to deliver each tier. All three publish to the same ESRI schema with an `accuracy_tier` field on every record — so you can mix tiers across the same network without data-merge headaches.

### Vision Lite (cloud SaaS) { #vision-lite }

For teams with archived dashcam, drone, or fleet video already on the shelf.

- No hardware shipped — cloud-only ingest
- Geo-tagged detections in your ESRI environment
- Screening-grade output; not for compliance audits
- Best for AEC archive mining and fleet-operator passive use

### Capture (iOS) { #capture }

For your field inspectors who currently walk with a clipboard.

- Sensor fusion: camera + GPS + IMU + ARKit/LiDAR
- Walking-pace or vehicle-mounted
- Works in GPS-denied environments
- Per-device monthly subscription

### LAIRA Rig (compliance-grade) { #rig }

For compliance-grade output.

- COTS sensor stack: Ouster + Septentrio + Premio + Lucid
- NVIDIA-accelerated edge inference < 200 ms / frame
- ±0.7 mm crack, ±3 mm elevation, ±2 cm RTK
- 35 lb on any operations vehicle · 10–15 min install

---

## When you need compliance-grade output { #datasheet }

The Rig is the deployment tier you contract for when your reporting requires ASTM&nbsp;D5340, ASTM&nbsp;D6433, UFC&nbsp;3-260-03, UFC&nbsp;3-270-08, FAA&nbsp;AC 150/53xx, or 23&nbsp;CFR&nbsp;490 compliance. Built on a COTS sensor stack; runs on your operations vehicle; publishes to your ArcGIS.

### LAIRA Rig v1 specifications

| Category | Specification |
|:---|:---|
| Status | Operationally deployed · TRL 7 |
| LiDAR | Ouster · 128-channel sliding-window SLAM |
| RGB Camera | Lucid · 4K, 1.67 mm/pix @ 3 m |
| GNSS | Septentrio RTK · ±2 cm WGS84 |
| Inertial | 6-axis IMU + VIO |
| Compute | Premio · NVIDIA edge |
| Inference | < 200 ms / frame |
| Speed | Up to 55 mph |
| Capture Width | ~55 m per pass |
| Mount | Any operations vehicle |
| Install Time | 10–15 minutes |
| Weight | ~35 lb |
| Endurance | 7 hr operating · 14 hr passthrough |

### Detection categories

**01 · Pavement Distress.** Cracks, raveling, weathering, depressions, faulting — classified and severity-scored per ASTM&nbsp;D5340 / D6433.

**02 · Foreign Object Debris.** FOD detection on runway, taxiway, and apron. Classified by material and risk.

**03 · Vegetation Encroachment.** Edge-of-pavement intrusion, AOA boundary monitoring, perimeter integrity.

**04 · Marking Degradation.** Wear, fading, calibrated retroreflectivity screening, MUTCD-grade classification.

### Resolution vs. standard threshold

| Metric | Specification |
|:---|:---|
| Crack-width resolution | ±0.7 mm (14× finer than D6433 §X1.14.2.2) |
| Elevation, faulting, depression | ±3 mm (below D6433 §X2.7 smallest threshold) |
| Rutting (transverse profile) | ±3 mm (30× finer than 23 CFR 490) |
| Geolocation (RTK GNSS) | ±2 cm (below D6433 §2.1.7 tolerance) |

### Standards coverage

- Pavement Condition Index (roads + lots) — ASTM&nbsp;D6433-20
- Airfield Pavement Condition Index — ASTM&nbsp;D5340
- Federal highway performance reporting — 23&nbsp;CFR Part 490
- Cracking / faulting / rutting methods — AASHTO R 85 / R 36 / R 48
- Sidewalk + curb-ramp geometric tolerances — PROWAG R302 / R304
- Roadway markings — MUTCD Part 3
- DoD pavement evaluation — UFC 3-260-03 / 3-270-08
- Airport markings & pavement maintenance — FAA AC 150/5340-1 / 5320-17

---

## Honesty block — what LAIRA Rig does NOT do

- Not a certified Class-1 inertial profiler today. AASHTO R 56 native certification is in active development. The Rig accepts your existing Greenwood, AMES, or ICC profiler IRI with cert chain preserved.
- Not a Falling Weight Deflectometer. Subsurface structural evaluation requires physical loading.
- Not a friction tester. Friction requires tire contact.
- Retroreflectivity is a calibrated screening estimate. Compliance audits still need handheld ASTM&nbsp;E1710 instrument readings.

---

## Proof — here's where it runs today

Four deployments across the two audiences that matter — DoW airfield management and AEC engineering business units — plus third-party validation from Esri.

### Wright-Patterson AFB · 88 OSS · AFCEC

Active beta-stage deployment supporting airfield inspection and reporting validation. FY26 procurement pathway via SBIR/AFWERX and direct commercial channels. *Major Ryan Samolewski · 88 OSS/OSAM*

### Haskell · AEC Engineering business unit

AEC engagement supporting pavement and right-of-way capture inside an active design and construction workflow. Engineering-led evaluation of LAIRA as a continuous-scan alternative to per-mile pavement data subcontracts and separate ADA surveys.

### San Bernardino International Airport · Beta operating partner · Featured by Esri (2026)

Active operational deployment since 2025. 3–7× more anomalies detected vs. manual; 50%+ reduction in field validation time; FAA Part 139 compliance baseline established. [See the full case study →](customers/sbd.md)

> "By deploying AI-driven airfield intelligence within our GIS environment, we are demonstrating how airports can move from reactive operations to predictive, data-led management."
>
> — Mike Burrows · CEO, San Bernardino International Airport · via Esri case study, 2026

### Moog Inc. · Defense Aviation · Federal subcontractor pathway

Letter of Intent for Airwai as a registered subcontractor on an SBIR D2P2 commercialization vehicle supporting Navy and FAA airfield inspection requirements.

---

## Next step

A pilot is one corridor of your choice, run on your operations vehicle, with outputs published directly to your existing ArcGIS environment. Audit-ready section report against the standards your team reports against, delivered inside 30 days.

[Schedule a pilot →](pricing.md#scope){ .md-button .md-button--primary }
