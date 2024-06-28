import demisto_client.demisto_api
from demisto_client.demisto_api import AutomationScript
from demisto_client.demisto_api.rest import ApiException
from dotenv import load_dotenv

load_dotenv()
api_instance = demisto_client.configure(debug=False)


def run_command(data: str, investigation_id: str) -> dict:
    update_entry = demisto_client.demisto_api.UpdateEntry(data=data,
                                                          investigation_id=investigation_id)  # UpdateEntry |  (optional)
    try:
        api_response = api_instance.investigation_add_entries_sync(update_entry=update_entry)
        return api_response
    except ApiException as e:
        print("Exception when calling DefaultApi->investigation_add_entries_sync: %s\n" % e)


def upload_script(script: str, name: str) -> dict:
    script = AutomationScript(script="print('hello world')", name="hello_world")
    automation_script_filter_wrapper = demisto_client.demisto_api.AutomationScriptFilterWrapper(script=script)

    try:
        api_response = api_instance.save_or_update_script(
            automation_script_filter_wrapper=automation_script_filter_wrapper)
        return api_response
    except ApiException as e:
        print("Exception when calling DefaultApi->save_or_update_script: %s\n" % e)


if __name__ == "__main__":
    run_command(data="!Print value=\"Test\"", investigation_id="17070")
