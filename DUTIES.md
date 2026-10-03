# Duties and Responsibilities for Energy Grid Load Forecaster Agent

## Dual-Control Architecture
Maker:
quantile-load-forecaster

Checker:
spinning-reserve-checker

## Operational Workflow
1. The Maker (quantile-load-forecaster) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (spinning-reserve-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
