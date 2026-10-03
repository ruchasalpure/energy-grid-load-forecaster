# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
quantile-load-forecaster

Checker:
spinning-reserve-checker

## Coordination Protocol
- **Primary Agent**: energy-grid-load-forecaster
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
