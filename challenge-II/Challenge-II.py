from RPA.Browser.Selenium import Selenium
from RPA.Tables import Tables
import time
from RPA.Archive import Archive
from RPA.Dialogs import Dialogs
from RPA.Robocorp.Vault import FileSecrets


class Title:

    def __init__(self):
        self.dialogs = Dialogs()
        self.browser = Selenium()
        self.tables = Tables()
        self.lib = Archive()
        self.listt = []
        self.secret = FileSecrets()

    def dialog(self):
        self.dialogs.add_heading("Upload CSV File")
        self.dialogs.add_file_input(label="Upload File", name="fileupload", file_type="CSV file(*.csv)")
        self.dialogs.add_submit_buttons("Submit")
        self.data = self.dialogs.run_dialog()

    def open_browser(self):
        secret = self.secret.get_secret("link")
        self.open_browser = self.browser.open_available_browser(f'{secret["url_link"]}')

    def order_robot(self):
        try:
            for ele in self.listt:
                self.browser.click_button('OK')
                self.browser.select_from_list_by_value('head', f'{ele["Head"]}')
                self.browser.select_radio_button('body', f'{ele["Body"]}')
                self.browser.input_text('//html/body/div/div/div[1]/div/div[1]/form/div[3]/input', f'{ele["Legs"]}')
                self.browser.input_text('address', f'{ele["Address"]}')
                self.browser.click_button("preview")
                self.browser.click_button('order')
                while True:
                    try:
                        self.browser.find_element("order-another")
                        break
                    except:
                        self.browser.click_button('order')
                self.browser.screenshot('robot-preview-image', f'output/robot+{ele["Order number"]}.png')
                time.sleep(3)
                self.browser.screenshot('receipt', f'output/robot+{ele["Order number"]}.png')
                self.browser.click_button('order-another')
        except:
            pass

    def read_file(self):
        var = self.tables.read_table_from_csv(self.data.fileupload[0],
                                              columns=["Order number", "Head", "Body", "Legs", "Address"])
        print(var)
        for ele in var:
            self.listt.append(ele)

    def archive(self):
        self.lib.archive_folder_with_tar('./output', 'output.tar', recursive=True)
        self.lib.list_archive('output.tar')


if __name__ == "__main__":
    title_obj = Title()
    title_obj.dialog()
    title_obj.open_browser()
    title_obj.read_file()
    title_obj.order_robot()
    title_obj.archive()
    print(title_obj.listt)
