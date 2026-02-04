# B12 Application Submission

This repository contains my submission for the **Full-Stack Engineer** role at **B12**.  

## Purpose

B12 requires applicants to submit a small automated script that:

1. Sends a signed POST request to the B12 application endpoint.  
2. Provides personal details, resume link, GitHub repository, and CI run link.  
3. Prints a receipt confirming successful submission.  

This repository demonstrates how I implemented that process using **Python** and **GitHub Actions**.

## Repository Structure
```
.
├── submit.py                # Python script that builds and sends the payload
├── requirements.txt         # Python dependencies (requests)
└── .github/
    └── workflows/
        └── submit.yml      # GitHub Actions workflow to run the script
```


## How It Works

1. The **submit.py** script constructs a JSON payload containing:
   - Name
   - Email
   - Resume link
   - Repository link
   - GitHub Actions run link
   - Timestamp (ISO 8601)
2. The payload is canonicalized (sorted keys, compact formatting).  
3. An **HMAC-SHA256 signature** is computed using the public signing secret.  
4. The script posts the payload to `https://b12.io/apply/submission` with the signature in the `X-Signature-256` header.  
5. The receipt from B12 is printed in the workflow logs.

## GitHub Actions

The workflow `.github/workflows/submit.yml` runs the submission automatically:

- Installs Python and dependencies.  
- Injects the correct GitHub Actions run link into `submit.py`.  
- Executes the submission script.  
- Prints the receipt confirming submission.

## Notes

- The `action_run_link` is dynamically generated during the workflow run.  
- The script ensures the JSON is compact and sorted, as required by B12.  
- The workflow can be triggered manually from the **Actions** tab.
