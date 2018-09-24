#!/usr/bin/env python3

import json
import pprint
from docxtpl import DocxTemplate
import secrets

pp = pprint.PrettyPrinter(indent=1, width=120)

doc = DocxTemplate("Vault_Statement_of_Work_Template_v0.6.1.docx")

context = secrets.context
pp.pprint(context)
doc.render(context)
doc.save("generated_scope.docx")
