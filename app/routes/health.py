from flask import Blueprint, jsonify
import datetime

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health_check():
    """
    /health — The most important endpoint in any DevOps project.
    CI/CD pipelines, Docker, Kubernetes, and load balancers all
    ping this to know if your app is alive and ready.
    Always return JSON with a status field.
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }), 200


@health_bp.route("/ready")
def readiness_check():
    """
    /ready — Tells the orchestrator the app is ready to receive traffic.
    You'd add DB connection checks, cache checks etc. here later.
    """
    checks = {
        "app": "ok",
        # "database": check_db(),   ← you'll add this later
    }
    all_ok = all(v == "ok" for v in checks.values())
    return jsonify({
        "status": "ready" if all_ok else "not ready",
        "checks": checks
    }), 200 if all_ok else 503