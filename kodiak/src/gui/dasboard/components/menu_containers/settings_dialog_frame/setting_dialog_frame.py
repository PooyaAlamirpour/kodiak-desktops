"""
    - Created on May 18/2020 - hacktorco
    - All rights reserved for hacktor team
"""

from PyQt5.QtWidgets import (QFrame, QLabel)
from PyQt5.QtCore import (Qt, QRect, QPropertyAnimation, QEasingCurve)
from PyQt5.QtGui import (QPixmap, QCursor)

from commons.constants.app_paths import AppPaths
from .setting_dialog_frame_styles import SettingDialogFrameStyles
from .....utils.utils_clicked_event import UtilsClick


class SettingDialogFrame:

    def __init__(self, containers: QFrame):
        super(SettingDialogFrame, self).__init__()
        self.containers = containers
        self.frame_concat_to_frame_setting = QFrame(self.containers)
        self.frame_concat_to_frame_setting.resize(161, 78)
        self.frame_concat_to_frame_setting.setStyleSheet(SettingDialogFrameStyles.all_frame_style)
        self.frame_concat_to_frame_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_concat_to_frame_setting.setFrameShadow(QFrame.Raised)
        self.frame_concat_to_frame_setting.setObjectName("frame_concat_to_frame_setting")

        self.frame_setting = QFrame(self.containers)
        self.frame_setting.resize(68, 78)
        self.frame_setting.setStyleSheet(SettingDialogFrameStyles.all_frame_style)
        self.frame_setting.setObjectName("frame_setting")
        self.frame_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_setting.setFrameShadow(QFrame.Raised)
        self.ease_out = QEasingCurve(QEasingCurve.OutQuad)
        self.ease_in = QEasingCurve(QEasingCurve.InQuad)

    def setup_ui(self):

        self.lbl_close_frame_setting = QLabel(self.frame_concat_to_frame_setting)
        self.lbl_close_frame_setting.setGeometry(QRect(5, 5, 21, 21))
        self.lbl_close_frame_setting.setCursor(QCursor(Qt.PointingHandCursor))

        self.lbl_close_frame_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/close_logo.svg"))
        self.lbl_close_frame_setting.setObjectName("lbl_close_frame_setting")
        UtilsClick.clickable(self.lbl_close_frame_setting).connect(
            lambda: self.set_visibility_effect(True, False, True))

        self.card_plugin = QLabel(self.frame_concat_to_frame_setting)
        self.card_plugin.setText("Add Plugin")
        self.card_plugin.setGeometry(QRect(40, 20, 71, 46))
        self.card_plugin.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_plugin.setStyleSheet(SettingDialogFrameStyles.cards_in_frame_style)
        self.card_plugin.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.card_plugin.setObjectName("card_plugin")

        self.pic_plugin_logo = QLabel(self.frame_concat_to_frame_setting)
        self.pic_plugin_logo.setGeometry(QRect(55, 5, 41, 31))
        self.pic_plugin_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pic_plugin_logo.setStyleSheet(SettingDialogFrameStyles.transparent_color_style)
        self.pic_plugin_logo.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/plugin_icon.svg"))
        self.pic_plugin_logo.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.pic_plugin_logo.setObjectName("pic_plugin_logo")

        self.lbl_setting = QLabel(self.frame_setting)
        self.lbl_setting.setText("Setting")
        self.lbl_setting.setGeometry(QRect(0, 27, 68, 21))
        self.lbl_setting.setStyleSheet(SettingDialogFrameStyles.lbl_frames_style)
        self.lbl_setting.setAlignment(Qt.AlignCenter)
        self.lbl_setting.setObjectName("lbl_setting")

        self.lbl_ellipse_setting = QLabel(self.frame_setting)
        self.lbl_ellipse_setting.setGeometry(QRect(0, 43, 68, 21))
        self.lbl_ellipse_setting.setPixmap(QPixmap(AppPaths.GUI_ASSETS_ICONS_PATH + "/main_window/ellipse_logo.svg"))
        self.lbl_ellipse_setting.setAlignment(Qt.AlignCenter)
        self.lbl_ellipse_setting.setObjectName("lbl_ellipse_setting")
        self.lbl_ellipse_setting.setStyleSheet(SettingDialogFrameStyles.transparent_color_style)

    def set_visibility_effect(self, visibility: bool, is_anime: bool, is_close: bool = False):
        """this method for set visibility  frame setting

        Arguments:
            visibility {bool} -- [this argument show status visibility frame ]
            is_anime {bool} -- [this argument show anime effect]

        Keyword Arguments:
            is_close {bool} -- [this argument when you want close frame] (default: {False})   
        """
        x_location_frame_setting: int = int(self.containers.width() - 81)

        x_location_frame_setting_concat: int = int(x_location_frame_setting + 10)

        if visibility and is_anime:
            # start animation
            self.do_anim_frame_setting(self.frame_setting,
                                       QRect(x_location_frame_setting, 360, 68, 78),
                                       QRect(x_location_frame_setting, 280, 68, 78)
                                       )
            self.do_anim_concat_frame_setting(
                self.frame_concat_to_frame_setting,
                QRect(x_location_frame_setting_concat-500, 360, 500, 168)
                , QRect(x_location_frame_setting_concat - self.frame_concat_to_frame_setting.width(), 280, 161, 78)
            )

        if is_close:
            # click button close animation
            self.do_anim_frame_setting(self.frame_setting,
                                       QRect(x_location_frame_setting, 280, 68, 78)
                                       , QRect(x_location_frame_setting + self.containers.width(), 280, 68, 78))

            self.do_anim_concat_frame_setting(
                self.frame_concat_to_frame_setting,
                QRect(x_location_frame_setting_concat, 280, 161, 78),
                QRect(x_location_frame_setting_concat + self.containers.width(), 280, 161, 78)
            )

        self.frame_setting.setVisible(visibility)
        self.frame_concat_to_frame_setting.setVisible(visibility)
        # delete from memory
        del x_location_frame_setting, x_location_frame_setting_concat

    def do_anim_frame_setting(self, obj: QFrame, start_location: QRect, end_location: QRect):

        """this method for do animation frame setting

        Arguments:
            obj {QFrame} -- [object must be do animation effect]
            start_location {QRect} -- [start location for anime]
            end_location {QRect} -- [end location for anime]
        """
        self.anim = QPropertyAnimation(obj, b"geometry")
        self.anim.setStartValue(start_location)
        self.anim.setEndValue(end_location)
        self.anim.setDuration(200)
        self.curve = QEasingCurve(QEasingCurve.OutQuad)
        self.anim.setEasingCurve(self.ease_out)
        self.anim.start()

    def do_anim_concat_frame_setting(self, obj: QFrame, start_location: QRect, end_location: QRect):

        """this method for do animation frame concat to frame setting

        Arguments:
            obj {QFrame} -- [object must be do animation effect]
            start_location {QRect} -- [start location for anime]
            end_location {QRect} -- [end location for anime]
        """
        self.anim_2 = QPropertyAnimation(obj, b"geometry")
        self.anim_2.setStartValue(start_location)
        self.anim_2.setEndValue(end_location)
        self.anim_2.setDuration(200)
        self.anim_2.setEasingCurve(self.ease_out)
        self.anim_2.start()