import json
from docxtpl import DocxTemplate

doc = DocxTemplate("scope_template.docx")
context = {
    "client": {
        "name" : "Doctor Stubb's Prosthetics n Orthotics, Inc., M.D.", 
        "contact": {
            "name": "Dr. Bigonnes P. Stubb"
        },
        "secondary_contact": {
            "name": "Johnsen P. Stubb"
        },
        "objectives_list": {"Maintain steady pace of installation, enhance security"}
    }, 
    "vendor": {
        "name": "Vault-O-Rama", 
        "services_agreement": {
            "final_date": "November 1, 2018"
        },
        "resources_list": {
            "minimum_hours": "60"
        },
        "engineer": {
            "role": "Vault Developer",
            "responsibilities": " * Install Vault",
            "location": "San Jose",
            "weekly_hours": "40",
            "hourly_rate": "$100",
            "resource_type": "FTE"
        },
        "manager": {
            "role": "Architect",
            "responsibilities": " * Supervise installation",
            "location": "San Jose",
            "weekly_hours": "20",
            "hourly_rate": "$250",
            "resource_type": "FTE"
        }
    },
    "project": {
        "soft_launch": "november",
        "full_launch": "december",
        "payment_basis": "Net 20",
        "minimum_resource_monthly_hours": "240"
    }
}
print(context)
doc.render(context)
doc.save("generated_scope.docx")
