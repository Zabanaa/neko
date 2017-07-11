# Neko

## Installation Instructions

1. (Optional but recommended) Create a virtual environment.

```bash
virtualenv -p python3 ENV__neko

source /path/to/projects/ENV__neko/bin.activate(.fish) # if you're using fish as a shell
```

2. Install dependencies

```bash
# Inside the project folder, run the following command:

pip install -r requirements.txt
```

3. Go grab your twitter api keys.

4. Open up `neko.sh` and populate the corresponding variables.

5. Get your Google Sheets OAuth Credentials from the Google Developer Console.

6. Save them at the top level of the project and rename the file
   `client_secret.json`.

7. Run the script (if you created a virtualenv, please make sure that it's
   activated).

8. Enjoy life.
