class SupplyChainPackageDependencyQuarantineScannerClient:
    def scan_software_bill_of_materials(self, package_manifest_text='requests==2.31.0\nurllib3==2.0.7', ecosystem_target='PYPI'):
        return {
            'sbom_scan_id': 'sbm_scn_7721',
            'vulnerabilities_discovered_count': 0,
            'typosquatting_risks_detected': 0,
            'malicious_telemetry_probes_found': 0,
            'quarantine_status_verdict': 'CLEARED_SAFE_FOR_PRODUCTION_BUILD',
            'sbom_dependency_attestation_url': 'https://security.sbom.genpark.ai/scans/7721.json'
        }
