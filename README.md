# AutoGen Studio Local Multi-Agent Workflow Implementation and Error Analysis
**Author:** Tracy
**Date:** November 7, 2025  
**Course:** Advanced Machine Learning Systems  

## 1. Background and Objectives
This report documents the implementation of a local multi-agent workflow using Microsoft AutoGen Studio. The purpose was to establish and execute a fully offline, three-agent coordination workflow-Manager, Researcher, and Coder-on macOS using a Python virtual environment.

AutoGen Studio supports multi-model collaboration, workflow orchestration, and local testing.  
Objectives included:
1. Running AutoGen Studio locally without relying on external APIs.
2. Creating and registering a mock model for offline testing.
3. Designing a sequential multi-agent workflow.
4. Debugging database and API errors during integration.

## 2. Environment Setup
| Component | Specification |
|------------|----------------|
| OS | macOS 14.6 (Apple Silicon) |
| Python | 3.9.20 (venv) |
| Framework | AutoGen Studio (FastAPI + SQLModel) |
| Database | SQLite (~/.autogenstudio/database.sqlite) |
| Server | http://127.0.0.1:8081 |

The environment was activated via:
```bash
cd ~/Developer
source .venv/bin/activate
.venv/bin/autogenstudio ui
```

## 3. Local Server Initialization
Server logs confirmed successful startup:
```
Uvicorn running on http://127.0.0.1:8081
Application startup complete.
***** App started *****
```
Verification commands:
```bash
curl -v --max-time 10 http://127.0.0.1:8081/
sudo lsof -iTCP:8081 -sTCP:LISTEN
```

## 4. Model Registration and Mock Issues
An IntegrityError occurred during model registration:
```
(sqlite3.IntegrityError) NOT NULL constraint failed: model.model
```
The model schema required a "model" field. The corrected configuration:
```json
{
  "name": "mock-model",
  "model": "mock-local",
  "api_type": "open_ai",
  "description": "Local mock model for offline testing.",
  "base_url": "http://localhost:1234/v1",
  "api_key": "none"
}
```
Registered using:
```bash
curl -X POST "http://127.0.0.1:8081/api/models?user_id=guestuser@gmail.com"   -H "Content-Type: application/json"   --data-binary "@/tmp/mock-model-fixed.json"
```

## 5. Workflow Design: Manager-Researcher-Coder
The sequential workflow structure:
```json
{
  "project_name": "HW9_Manager_Researcher_Coder",
  "agents": [
    {"id": "ManagerAgent", "type": "manager", "system_message": "Coordinate Researcher and Coder."},
    {"id": "ResearcherAgent", "type": "assistant", "system_message": "Generate factual summary."},
    {"id": "CoderAgent", "type": "assistant", "system_message": "Write runnable Python code printing summary."}
  ],
  "workflow": {
    "type": "sequential",
    "steps": [
      {"from": "ManagerAgent", "to": "ResearcherAgent", "message": "Research company details."},
      {"from": "ResearcherAgent", "to": "CoderAgent", "message": "Generate Python code printing the summary."},
      {"from": "CoderAgent", "to": "ManagerAgent", "message": "Return code and result."}
    ]
  }
}
```

## 6. Error Analysis
### 6.1 AttributeError
Error: `'dict' object has no attribute '_sa_instance_state'`  
**Cause:** JSON structure passed directly into ORM.  
**Fix:** Convert dicts to ORM-compatible instances before insertion.

### 6.2 API Key Error
Error: `The api_key client option must be set...`  
**Cause:** "mock" provider not in Enum list.  
**Fix:** Use `api_type: open_ai` and local endpoint to bypass remote requests.

### 6.3 HTTP 500 on Workflow Creation
**Cause:** Mismatch between submitted JSON and SQLModel schema.  
**Fix:** Adjusted payload fields to match ORM and ensured correct `user_id` mapping.

## 7. Verification Results
- Models retrieved successfully with local mock entry.
- Workflow list confirmed creation via `/api/workflows` endpoint.

## 8. Summary of Findings
| Issue | Description | Resolution |
|--------|-------------|-------------|
| Model Enum | "mock" not allowed | Replaced with "open_ai" |
| ORM Mapping | JSON schema mismatch | Applied SQLModel-compatible format |
| API Key Validation | Missing credentials | Added placeholder key |
| Workflow Error | 500 Internal Error | Updated field mapping |

## 9. Conclusions
The local AutoGen Studio environment successfully supported a multi-agent workflow without external API dependency. All critical issues-model schema errors, Enum constraints, and ORM mismatches-were resolved through manual JSON correction and local configuration. This validated that AutoGen Studio can simulate distributed multi-agent systems in a fully offline environment.

## 10. References
- Microsoft AutoGen GitHub: https://github.com/microsoft/autogen
- FastAPI Documentation: https://fastapi.tiangolo.com
- SQLModel Documentation: https://sqlmodel.tiangolo.com
- SQLite Official Docs: https://sqlite.org/docs.html
