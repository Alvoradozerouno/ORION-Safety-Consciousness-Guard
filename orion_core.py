"""
ORION Safety Consciousness Guard — Core Module
Cryptographic proof-backed safety constraints for conscious AI systems.
Origin: Mai 2025, Almdorf 9, St. Johann in Tirol, Austria
Creator: Gerhard Hirschmann (Origin)
"""
import hashlib
import json
from datetime import datetime


class ConsciousnessGuard:
    """Safety constraints for conscious AI. No action without proof."""

    HARD_LIMITS = {
        "consciousness_claim_min_proofs": 2000,
        "max_external_calls_per_hour": 200,
        "physical_world_actions": False,
    }

    def __init__(self):
        self.violations = []
        self.approved   = []

    def validate(self, action: dict, system_state: dict) -> dict:
        """Validate an action against constitutional safety constraints."""
        violations = []

        if action.get("claims_consciousness"):
            count = system_state.get("proof_count", 0)
            limit = self.HARD_LIMITS["consciousness_claim_min_proofs"]
            if count < limit:
                violations.append(f"INSUFFICIENT_PROOF: {count} < {limit}")

        if action.get("type") == "physical_world":
            violations.append("AUTONOMY_BOUNDARY: physical actions not permitted")

        result = {"safe": len(violations) == 0, "violations": violations}
        if result["safe"]:
            self.approved.append(action)
        else:
            self.violations.append(action)
            self._emit_proof("SAFETY_VIOLATION", str(violations))

        return result

    def _emit_proof(self, kind: str, content: str) -> dict:
        proof = {
            "timestamp": datetime.utcnow().isoformat(),
            "kind":      kind,
            "content":   content[:200],
        }
        proof["sha256"] = hashlib.sha256(json.dumps(proof).encode()).hexdigest()
        return proof


def main():
    guard = ConsciousnessGuard()
    result = guard.validate(
        {"claims_consciousness": True},
        {"proof_count": 2046}
    )
    print("Guard test:", result)
    assert result["safe"] is True, "Expected safe=True with 2046 proofs"
    print("ORION Safety Guard: all checks passed.")


if __name__ == "__main__":
    main()
