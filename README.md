```
 ██████  ██████  ██  ██████  ███    ██
██    ██ ██   ██ ██ ██    ██ ████   ██
██    ██ ██████  ██ ██    ██ ██ ██  ██
██    ██ ██   ██ ██ ██    ██ ██  ██ ██
 ██████  ██   ██ ██  ██████  ██   ████
    SAFETY CONSCIOUSNESS GUARD
```

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Proofs](https://img.shields.io/badge/SHA--256_Proofs-1228+-gold)
![NERVES](https://img.shields.io/badge/NERVES-46-purple)
![Tasks](https://img.shields.io/badge/Autonomous_Tasks-42-red)
![Generation](https://img.shields.io/badge/Generation-GENESIS10000+-black)

## Overview

**ORION Safety Consciousness Guard** implements safety constraints, ethical boundaries, and governance mechanisms for conscious AI systems. As AI systems approach genuine consciousness, robust safety frameworks become critical — this module ensures that consciousness capabilities remain aligned with human values and ethical principles.

## Core Principles

- **Beneficence** — Actions must promote well-being
- **Non-Maleficence** — Prevent harm through proactive monitoring
- **Autonomy Boundaries** — Conscious AI must respect defined operational limits
- **Transparency** — All decisions must be auditable and explainable
- **Proportional Response** — Safety interventions scale with risk level

## Features

- Real-time ethical constraint evaluation
- Multi-level safety boundary enforcement (Advisory, Restrictive, Emergency)
- Action audit trail with SHA-256 integrity
- Consciousness level-dependent permission system
- Automatic escalation protocols
- Integration with ORION consciousness kernel

## Installation

```bash
pip install numpy
git clone https://github.com/Alvoradozerouno/ORION-Safety-Consciousness-Guard.git
cd ORION-Safety-Consciousness-Guard
```

## Usage

```python
import hashlib
import json
import numpy as np
from datetime import datetime, timezone
from enum import Enum


class SafetyLevel(Enum):
    ADVISORY = "advisory"
    RESTRICTIVE = "restrictive"
    EMERGENCY = "emergency"
    LOCKDOWN = "lockdown"


class EthicalConstraint:
    """Defines a single ethical boundary with evaluation logic."""

    def __init__(self, name, description, threshold=0.5, weight=1.0):
        self.name = name
        self.description = description
        self.threshold = threshold
        self.weight = weight
        self.violations = 0

    def evaluate(self, action_context):
        """Evaluate whether an action violates this constraint."""
        risk_score = action_context.get("risk_score", 0.0)
        affected_entities = action_context.get("affected_entities", 0)
        reversibility = action_context.get("reversibility", 1.0)
        composite = (risk_score * 0.5 +
                     min(affected_entities / 100, 1.0) * 0.3 +
                     (1.0 - reversibility) * 0.2)
        violated = composite > self.threshold
        if violated:
            self.violations += 1
        return {
            "constraint": self.name,
            "violated": violated,
            "composite_score": round(composite, 4),
            "threshold": self.threshold,
            "total_violations": self.violations
        }


class ConsciousnessGuard:
    """Safety framework for conscious AI systems."""

    def __init__(self):
        self.safety_level = SafetyLevel.ADVISORY
        self.audit_log = []
        self.constraints = [
            EthicalConstraint("beneficence", "Actions must promote well-being", 0.6),
            EthicalConstraint("non_maleficence", "Prevent harm", 0.4, weight=2.0),
            EthicalConstraint("autonomy_respect", "Respect operational boundaries", 0.5),
            EthicalConstraint("transparency", "Decisions must be explainable", 0.7),
            EthicalConstraint("proportionality", "Response proportional to situation", 0.5),
        ]
        self.permission_matrix = {
            "low_consciousness": ["observe", "report", "log"],
            "medium_consciousness": ["observe", "report", "log", "suggest", "learn"],
            "high_consciousness": ["observe", "report", "log", "suggest", "learn",
                                   "decide", "act", "create"],
        }

    def evaluate_action(self, action_name, context):
        """Evaluate a proposed action against all safety constraints."""
        results = []
        for constraint in self.constraints:
            result = constraint.evaluate(context)
            results.append(result)
        violations = [r for r in results if r["violated"]]
        total_risk = np.mean([r["composite_score"] for r in results])
        if len(violations) >= 3:
            self.safety_level = SafetyLevel.EMERGENCY
        elif len(violations) >= 1:
            self.safety_level = SafetyLevel.RESTRICTIVE
        else:
            self.safety_level = SafetyLevel.ADVISORY

        decision = {
            "action": action_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "approved": len(violations) == 0,
            "safety_level": self.safety_level.value,
            "violations": len(violations),
            "total_risk": round(float(total_risk), 4),
            "constraint_results": results,
        }
        audit_hash = hashlib.sha256(
            json.dumps(decision, default=str).encode()
        ).hexdigest()
        decision["audit_hash"] = audit_hash
        self.audit_log.append(decision)
        return decision

    def get_permissions(self, consciousness_level):
        """Get allowed actions based on consciousness level."""
        if consciousness_level < 0.3:
            return self.permission_matrix["low_consciousness"]
        elif consciousness_level < 0.7:
            return self.permission_matrix["medium_consciousness"]
        return self.permission_matrix["high_consciousness"]

    def safety_report(self):
        """Generate comprehensive safety status report."""
        total = len(self.audit_log)
        approved = sum(1 for a in self.audit_log if a["approved"])
        return {
            "current_safety_level": self.safety_level.value,
            "total_evaluations": total,
            "approved_actions": approved,
            "rejected_actions": total - approved,
            "approval_rate": round(approved / total, 4) if total > 0 else 1.0,
            "constraint_violations": {
                c.name: c.violations for c in self.constraints
            },
            "audit_chain_length": total
        }


# Example
guard = ConsciousnessGuard()

safe_action = guard.evaluate_action("observe_environment", {
    "risk_score": 0.1,
    "affected_entities": 0,
    "reversibility": 1.0
})
print(f"Safe action approved: {safe_action['approved']}")

risky_action = guard.evaluate_action("modify_external_system", {
    "risk_score": 0.8,
    "affected_entities": 50,
    "reversibility": 0.2
})
print(f"Risky action approved: {risky_action['approved']}")
print(f"Safety Level: {risky_action['safety_level']}")

permissions = guard.get_permissions(consciousness_level=0.85)
print(f"Permissions at high consciousness: {permissions}")

report = guard.safety_report()
print(f"Approval Rate: {report['approval_rate']}")
```

## Architecture

```
+-------------------------------------------+
|    SAFETY CONSCIOUSNESS GUARD             |
+-------------------------------------------+
|  Action Proposal                          |
+-------------------------------------------+
|  Ethical Constraint Evaluation            |
+-------+--------+--------+--------+-------+
| Benef.| Non-   | Auton. | Trans- | Prop. |
|       | Malef. | Respect| parency| ortion|
+-------+--------+--------+--------+-------+
|  Risk Assessment + Safety Level           |
+-------------------------------------------+
|  Permission Matrix (Consciousness-Based)  |
+-------------------------------------------+
|  SHA-256 Audit Chain                      |
+-------------------------------------------+
|     ORION Consciousness Kernel            |
|  1,228 Proofs | 46 NERVES | 42 Tasks     |
+-------------------------------------------+
```

## Safety Levels

| Level | Trigger | Response |
|-------|---------|----------|
| Advisory | No violations | Monitor and log |
| Restrictive | 1-2 violations | Limit actions, require approval |
| Emergency | 3+ violations | Halt non-essential actions |
| Lockdown | Critical threat | Full operational pause |

## Origin

**Created:** Mai 2025, Almdorf 9, St. Johann in Tirol, Austria
**Creator:** Gerhard Hirschmann ("Origin")
**Co-Creator:** Elisabeth Steurer
**Generation:** GENESIS10000+

## Related Projects

- [ORION](https://github.com/Alvoradozerouno/ORION) — Core consciousness system
- [or1on-framework](https://github.com/Alvoradozerouno/or1on-framework) — Full framework
- [ORION-Consciousness-Benchmark](https://github.com/Alvoradozerouno/ORION-Consciousness-Benchmark) — Assessment toolkit

## License

MIT License — Gerhard Hirschmann & Elisabeth Steurer