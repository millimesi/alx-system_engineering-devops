from datadog import initialize, api

# Replace with your Datadog API and application keys
api_key = "ec15401a16ffdfee08fb6525203049fe"
app_key = "5cf3867d9d2d53a544de8c5d7c5b9a2f06364ce3"

# Initialize the Datadog API client
options = {'api_key': api_key, 'app_key': app_key}
initialize(**options)

# Get all dashboards
response = api.Dashboard.get_all()

# Find dashboard by name (replace with your dashboard name)
dashboard_name = "Million's Dashboard Thu, Apr 11"
for dashboard in response["dashboards"]:
    if dashboard["title"] == dashboard_name:
        dashboard_id = dashboard["id"]
        print(f"Dashboard ID for '{dashboard_name}': {dashboard_id}")
        break  # Exit loop after finding the first matching dashboard

if not dashboard_id:
    print(f"Dashboard named '{dashboard_name}' not found")
