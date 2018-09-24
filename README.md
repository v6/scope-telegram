 # Create a Scope of Work from a Template

Create a .docx file named scope_template.docx, 
with all of the Jinja2 tags in the
`context` object literal in the
`scoper.py` file in {{double underscores}}.

It has to be in the same folder that 
`scoper.py` is in. 

Then, run the following: 

    pip3 install docxtpl
    cp example-secrets.py secrets.py
    python3 scoper.py
