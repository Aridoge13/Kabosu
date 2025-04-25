# Security Policy

## Supported Versions
Kabosu is currently under active development. Security updates are applied to the latest version of the codebase.  
**Supported**: `main` branch (latest commit).  
**Unsupported**: Older branches or forks.

---

## Reporting a Vulnerability
If you discover a security vulnerability in Kabosu, **please report it responsibly**:
1. **Do not open a public issue** on GitHub.
2. Email the maintainers at: `aritra.mukherjee98@gmail.com` with:
   - A detailed description of the vulnerability.
   - Steps to reproduce (if applicable).
   - Your name/handle for acknowledgement (optional).

**Response Time**: We aim to acknowledge reports within 72 hours and provide a resolution timeline.

---

## Security Considerations
Kabosu handles sensitive genomic/clinical data. Key safeguards include:
- **Data Anonymization**: All example datasets in the repository are anonymized.
- **No Hardcoded Credentials**: Never commit API keys, tokens, or patient data to the repo.
- **Dependency Audits**: Regular scans for vulnerable dependencies (e.g., using `pip-audit` or GitHub Dependabot).

---

## User Responsibilities
To ensure secure usage:
1. **Local Data**: If processing private data, ensure files are stored securely.
2. **Permissions**: Restrict access to input/output files on shared systems.
3. **Updates**: Regularly pull the latest version of Kabosu for security patches.

---

## Known Limitations
- Kabosu is designed for research use and **not yet HIPAA/GDPR-compliant** for clinical deployment.
- Web interfaces (will be added later) will require HTTPS and user authentication.

---

## Acknowledgments
We credit security researchers who responsibly disclose vulnerabilities.  
