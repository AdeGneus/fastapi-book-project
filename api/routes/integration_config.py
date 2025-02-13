from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

integration_json = {
    "data": {
        "date": {
            "created_at": "2025-02-13",
            "updated_at": "2025-02-13"
        },
        "descriptions": {
            "app_name": "Telex-FastAPI",
            "app_description": "Forwards Telex CI/CD notifications to Slack",
            "app_logo": "http://ec2-13-60-216-247.eu-north-1.compute.amazonaws.com",
            "app_url": "http://ec2-13-60-216-247.eu-north-1.compute.amazonaws.com",
            "background_color": "#fff"
        },
        "is_active": True,
        "integration_type": "text",
        "key_features": [
            "Real-time updates",
            "Slack notifications"
        ],
        "author": "Wasiu Bakare",
        "settings": [
            {
                "label": "Slack Channel",
                "type": "text",
                "required": True,
                "default": "#devops-alert"
            },
            {
                "label": "Time Interval",
                "type": "dropdown",
                "required": True,
                "default": "Immediate",
                "options": [
                    "Immediate",
                    "Every 5 mins",
                    "Hourly"
                ]
            },
            {
                "label": "Event Type",
                "type": "dropdown",
                "required": True,
                "default": "ci_pipeline",
                "options": [
                    "ci_pipeline",
                    "deployment",
                    "error"
                ]
            },
            {
                "label": "Message Format",
                "type": "text",
                "required": True,
                "default": "Basic"
            },
            {
                "label": "Include Logs",
                "type": "checkbox",
                "required": True,
                "default": True
            }
        ],
        "target_url": "https://hooks.slack.com/services/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",
        "tick_url": "http://ec2-13-60-216-247.eu-north-1.compute.amazonaws.com/telex-webhook"
    }
}

@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)
