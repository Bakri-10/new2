import tableauserverclient as TSC

# Tableau Server details
server_url = 'https://your-tableau-server.com'
personal_access_token_name = 'your-token-name'
personal_access_token_value = 'your-token-value'
site = ''  # Leave empty for the default site, or set the site name if needed

# Set up authentication using the PAT
tableau_auth = TSC.TableauAuth(personal_access_token_name, personal_access_token_value, site)
server = TSC.Server(server_url, use_server_version=True)

# Sign in to Tableau Server using the PAT
server.auth.sign_in(tableau_auth)

# Get all views
all_views, pagination_item = server.views.get()

# Loop through views and print view id and name
for view in all_views:
    print(f"View Name: {view.name}, View ID: {view.id}")

# Sign out
server.auth.sign_out()
