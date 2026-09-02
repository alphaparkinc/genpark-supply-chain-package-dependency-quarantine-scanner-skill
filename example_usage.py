from client import SupplyChainPackageDependencyQuarantineScannerClient

def main():
    client = SupplyChainPackageDependencyQuarantineScannerClient()
    res = client.scan_software_bill_of_materials('flask==3.0.0', 'PYPI')
    print('Supply Chain Quarantine Scanner: ' + res['sbom_scan_id'] + ' (' + res['quarantine_status_verdict'] + ')')
    print('Vulnerabilities: ' + str(res['vulnerabilities_discovered_count']) + ' | Typosquatting: ' + str(res['typosquatting_risks_detected']))
    print('Attestation URL: ' + res['sbom_dependency_attestation_url'])

if __name__ == '__main__':
    main()
