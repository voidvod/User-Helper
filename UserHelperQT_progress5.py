### Import Section Start
import os
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
### Import Section End

##### Global Variables start
Pass_value = ''

#### File read start
Error_log = open('Error_log.txt', 'a')

file_read = open('_internal/Util/packagemanager.list', "r")
packmanager_data = file_read.read()
file_read.close()

packmanager_list = packmanager_data.splitlines()
nr_pckgmngr = len(packmanager_list)
percent = (1/nr_pckgmngr) * 100

#### File read end
##### Global Variables end


### Class / Define Start
class Progress_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Progress")
        self.progress_window_ui()

    def progress_window_ui(self):
        progress_window_layout = QVBoxLayout()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(200, 80, 300, 30)  # Adjusted size
        progress_window_layout.addWidget(self.progress_bar)
        self.setLayout(progress_window_layout)
        self.setFixedSize(400, 100)  # Set fixed size for the progress window

    def center_below_parent(self, parent):
        parent_geometry = parent.geometry()
        x = parent_geometry.x() + (parent_geometry.width() - self.width()) // 2
        y = parent_geometry.y() + parent_geometry.height()
        self.move(x, y)

class Password_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password")
        self.password_window_ui()

    def password_window_ui(self):
        password_window_layout = QVBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMaxLength(16)
        self.password_input.setPlaceholderText("Enter your password")

        password_window_layout.addWidget(self.password_input)
        self.password_input.returnPressed.connect(self.save_password)
        self.setLayout(password_window_layout)
        self.setGeometry(100, 100, 300, 100)
        self.center_window()

    def save_password(self):
        global Pass_value
        Pass_value = self.password_input.text()
        self.accept()

    def center_window(self):
        screen_geometry = QScreen.availableGeometry(QApplication.primaryScreen())
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

class UpdateWorker(QThread):
    progressChanged = pyqtSignal(int)
    workFinished = pyqtSignal()

    def __init__(self, password, packmanager_list, percent):
        super().__init__()
        self.password = password
        self.packmanager_list = packmanager_list
        self.percent = percent

    def run(self):
        progress_value = 0
        for packmanager in self.packmanager_list:
            self.update_and_upgrade(self.password, packmanager)
            progress_value += self.percent
            self.progressChanged.emit(int(progress_value))
        self.workFinished.emit()

    def update_and_upgrade(self, password, packmanager):
        cmd = os.system("which " + packmanager)
        cmd_upd = f'echo {password} | sudo -S {packmanager} update'
        cmd_upg = f'echo {password} | sudo -S {packmanager} upgrade -y'
        if cmd != 256:
            if packmanager in ["apt", "apt-get", "nala"]:
                os.system(cmd_upd)
                os.system(cmd_upg)
            elif packmanager in ["dnf"]:
                os.system(cmd_upd)
                dnf_update = f'echo {password} | sudo -S {packmanager} update'
                os.system(dnf_update)
                dnf_run = f'echo {password} | sudo -S {packmanager} update -y'
                os.system(dnf_run)
            elif packmanager in ["snap"]:
                snap_update = f'echo {password} | sudo -S {packmanager} refresh'
                os.system(snap_update)
            elif packmanager in ["yum"]:
                yum_update = f'echo Pass | sudo -S {packmanager} check-update'
                os.system(yum_update)
                os.system(cmd_upd)
                os.system(cmd_upg)
            elif packmanager in ["zypper"]:
                zypper_upd_b_upg = f'echo {password} | sudo -S {packmanager} refresh && sudo -S {packmanager} update '
                os.system(zypper_upd_b_upg)
                zypper_upg = f'echo {password} | sudo -S {packmanager} up'
                os.system(zypper_upg)
            elif packmanager in ["pip"]:
                pip_upd = f'{packmanager} install --upgrade pip'
                os.system(pip_upd)
            elif packmanager in ["flatpak"]:
                os.system(cmd_upd)
            elif packmanager in ["apk-tools", "apk"]:
                apk_upd = f'echo {password} |sudo -S apk update && upgrade -y'
                os.system(apk_upd)

class CleanWorker(QThread):
    progressChanged = pyqtSignal(int)
    workFinished = pyqtSignal()

    def __init__(self, password, packmanager_list, percent):
        super().__init__()
        self.password = password
        self.packmanager_list = packmanager_list
        self.percent = percent

    def run(self):
        progress_value = 0
        for packmanager in self.packmanager_list:
            self.system_clean(self.password, packmanager)
            progress_value += self.percent
            self.progressChanged.emit(int(progress_value))
        self.workFinished.emit()

    def system_clean(self, password, packmanager):
        cmd = os.system("which " + packmanager)
        cmd_clean = f'echo {password} | sudo -S {packmanager} autoremove -y'

        if cmd != 256:
            if packmanager in ["apt", "apt-get", "nala"]:
                os.system(cmd_clean)
            elif packmanager in ["dnf"]:
                os.system(cmd_clean)
            elif packmanager in ["snap"]:
                os.system("pushd ./_internal")
                os.system("pushd ./Util")
                snap_cmd = f'echo {password} | sudo -S bash Snap_clean.sh'
                os.system("popd")
                os.system("popd")
            elif packmanager in ["yum"]:
                os.system(cmd_clean)
            elif packmanager in ["zypper"]:
                zypper_clean = f'echo {password} | sudo -S {packmanager} cc -a'
                os.system(zypper_clean)
            elif packmanager in ["flatpak"]:
                flatpak_clean = f'{packmanager} uninstall --unused'
                flatpak_repair = f'{packmanager} repair'
                os.system(flatpak_clean)
                os.system(flatpak_repair)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.win = QWidget()
        self.setCentralWidget(self.win)
        self.setWindowTitle(" User Helper ")
        self.mainwindow_ui_components()
        self.setGeometry(100, 100, 400, 300)  # Adjusted size
        self.center_window()

    def mainwindow_ui_components(self):
        update_button = QPushButton(" Update system ")
        system_clean_button = QPushButton(" System Clean ")
        settings_button = QPushButton(" Settings ")
        exit_button = QPushButton(" Exit ")

        layout = QVBoxLayout()
        layout.addWidget(update_button)
        layout.addWidget(system_clean_button)
        layout.addWidget(settings_button)
        layout.addWidget(exit_button)

        self.win.setLayout(layout)

        update_button.clicked.connect(self.update_button_action)
        system_clean_button.clicked.connect(self.system_clean_button_action)
        settings_button.clicked.connect(self.settings_menu)
        exit_button.clicked.connect(self.exit_action)

    def settings_menu(self):
        print('Settings menu comes here')

    def exit_action(self):
        app.quit()

    def show_password_window(self):
        if Pass_value == '':
            self.password_window = Password_Window()
            self.password_window.exec()
        else:
            pass

    def show_progress_window(self):
        self.progress_window = Progress_Window(self)
        self.progress_window.center_below_parent(self)
        self.progress_window.show()

    def update_button_action(self):
        self.show_password_window()
        self.show_progress_window()

        self.update_thread = UpdateWorker(Pass_value, packmanager_list, percent)
        self.update_thread.progressChanged.connect(self.progress_window.progress_bar.setValue)
        self.update_thread.workFinished.connect(self.on_update_finished)
        self.update_thread.start()

    def on_update_finished(self):
        self.show_message_box("Update", "System update completed!")

    def system_clean_button_action(self):
        self.show_password_window()
        self.show_progress_window()

        self.clean_thread = CleanWorker(Pass_value, packmanager_list, percent)
        self.clean_thread.progressChanged.connect(self.progress_window.progress_bar.setValue)
        self.clean_thread.workFinished.connect(self.on_clean_finished)
        self.clean_thread.start()

    def on_clean_finished(self):
        self.show_message_box("Clean", "System clean completed!")

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.finished.connect(self.progress_window.close)
        msg_box.exec()

    def center_window(self):
        screen_geometry = QScreen.availableGeometry(QApplication.primaryScreen())
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

### Main App loop start
if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
### Main App loop end
