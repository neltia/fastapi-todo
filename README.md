# fastapi-todo

### Preferences

- active venv

<pre>
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
</pre>

- config file
    - UNKEY_ROOT_KEY: unkey service(https://www.unkey.com/) your root key
    - UNKEY_API_ID: Unique ID of the API created in unkey workspace

<pre>
UNKEY_ROOT_KEY=unkey_~
UNKEY_API_ID=api_~
</pre>


### Run Program
- dev program run
<pre>
python main.py
</pre>

### Manual
/verify
- x-api_key: Key to use API issued by unkey (enter key value, not keyId)
